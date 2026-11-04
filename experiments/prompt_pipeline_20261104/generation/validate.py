"""Offline prompt lineage, MySQL-dialect parsing, and independent expected-row checks.

Requires sqlglot (validated with 30.17.0). No database or network access.
PREPARE/EXECUTE/DEALLOCATE controls are checked separately; their SELECTs are parsed.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re

import sqlglot
from sqlglot import exp
from sqlglot.tokens import TokenType

ROOT = Path(__file__).resolve().parent


def read(path):
    return (ROOT/path).read_text(encoding="utf-8")


def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def literal(node):
    if isinstance(node, exp.Null):
        return None
    if isinstance(node, exp.Literal):
        return node.this if node.is_string else int(node.this)
    if isinstance(node, exp.Introducer):
        return literal(node.expression)
    if isinstance(node, (exp.Collate, exp.Paren)):
        return literal(node.this)
    raise AssertionError(f"Not a supported fixture literal: {node!r}")


def parse_select(text):
    ast = sqlglot.parse_one(text, read="mysql", error_level=sqlglot.ErrorLevel.RAISE)
    assert isinstance(ast, exp.Select), type(ast)
    return ast


def statements(text):
    previous = 0
    for token in sqlglot.Dialect.get_or_raise("mysql").tokenize(text):
        if token.token_type == TokenType.SEMICOLON:
            part = text[previous:token.start]
            previous = token.end + 1
            part = re.sub(r"\A(?:\s*--[^\n]*(?:\n|$))*\s*", "", part).strip()
            if part:
                yield part
    assert not re.sub(r"--[^\n]*", "", text[previous:]).strip(), "Unterminated statement"


def inspect_sql(text):
    tables, prepared, variables, settings = {}, {}, {}, {}
    pending, records = None, []
    parsed_types = Counter()
    controls = Counter()
    created, dropped = set(), set()
    for stmt in statements(text):
        prepare = re.fullmatch(r"PREPARE (\w+) FROM '((?:[^']|'')*)'", stmt, re.S | re.I)
        execute = re.fullmatch(r"EXECUTE (\w+)(?: USING (@\w+))?", stmt, re.I)
        deallocate = re.fullmatch(r"DEALLOCATE PREPARE (\w+)", stmt, re.I)
        if prepare:
            name, query = prepare.groups()
            assert name not in prepared
            prepared[name] = parse_select(query.replace("''", "'"))
            controls["PREPARE"] += 1
            continue
        elif execute:
            name, parameter = execute.groups()
            assert name in prepared
            ast = prepared[name]
            count = len(list(ast.find_all(exp.Placeholder)))
            assert count == (1 if parameter else 0)
            if parameter:
                assert parameter in variables
            controls["EXECUTE"] += 1
        elif deallocate:
            assert deallocate[1] in prepared
            del prepared[deallocate[1]]
            controls["DEALLOCATE PREPARE"] += 1
            continue
        else:
            ast = sqlglot.parse_one(stmt, read="mysql", error_level=sqlglot.ErrorLevel.RAISE)
            assert not isinstance(ast, exp.Command), f"Unparsed statement: {stmt}"
            parsed_types[type(ast).__name__] += 1
        if isinstance(ast, exp.Create):
            table = ast.find(exp.Table).name
            assert table not in created
            created.add(table)
        elif isinstance(ast, exp.Insert):
            table = ast.this.name
            assert isinstance(ast.expression, exp.Values)
            tables[table] = [[literal(x) for x in row.expressions] for row in ast.expression.expressions]
        elif isinstance(ast, exp.Drop):
            table = ast.this.name
            assert table in created, "Drop of a table not created by this script"
            dropped.add(table)
        elif isinstance(ast, exp.Delete):
            assert ast.this.name == "wf_248_lookup"
            assert ast.args["where"].sql(dialect="mysql").upper() == "WHERE K IS NULL"
            tables[ast.this.name] = [r for r in tables[ast.this.name] if r[0] is not None]
        elif isinstance(ast, exp.Set):
            binding = re.fullmatch(r"SET (@\w+) = (\d+)", stmt, re.I)
            if binding:
                variables[binding[1]] = int(binding[2])
            switch = re.fullmatch(r"SET SESSION optimizer_switch = 'derived_condition_pushdown=(on|off)'", stmt,re.I)
            if switch:
                settings["pushdown"] = switch[1].lower()
            precision = re.fullmatch(r"SET SESSION windowing_use_high_precision = (ON|OFF)",stmt,re.I)
            if precision:
                settings["high_precision"] = precision[1].upper()
        elif isinstance(ast, exp.Select):
            if ast.named_selects == ["case_id"]:
                assert pending is None
                pending = literal(ast.expressions[0].this)
            elif pending is not None:
                assert ast.args.get("order") is not None
                records.append({"label":pending,"ast":ast,"tables":deepcopy(tables),
                                "variables":dict(variables),"settings":dict(settings),
                                "execute":bool(execute)})
                pending = None
    assert pending is None and not prepared
    assert created == dropped
    return records, dict(parsed_types), dict(controls)


def charset_oracle(record):
    ast = record["ast"]
    suffix = literal(ast.find(exp.Concat).expressions[1])
    target = literal(ast.args["where"].this.expression)
    rows = []
    for ident,value in record["tables"]["wf_4d2_text"]:
        if value is None:
            continue
        tag = value + suffix
        if tag == target:
            rows.append([ident,tag.encode("utf-8").hex().upper(),len(tag),len(tag.encode("utf-8"))])
    return sorted(rows)


def property_oracle(record):
    partitions = defaultdict(list)
    for group,ident,value in record["tables"]["wf_248_values"]:
        partitions[group].append((ident,value))
    is_in = record["ast"].find(exp.In) is not None
    if is_in:
        offset = 1
        lookup = [r[0] for r in record["tables"]["wf_248_lookup"]]
    elif record["execute"]:
        offset = record["variables"]["@wf_248_offset"]
    else:
        offset = literal(record["ast"].expressions[2].this.this)
    output = []
    for group,part in sorted(partitions.items()):
        part.sort()
        for pos,(ident,_) in enumerate(part):
            frame = [v for _,v in part[pos:pos+2] if v is not None]
            wrapped = sum(frame) + offset if frame else None
            if is_in:
                truth = None if wrapped is None else (1 if wrapped in lookup else None if None in lookup else 0)
                output.append([group,ident,wrapped,truth])
            else:
                output.append([group,ident,wrapped,len(part)-pos])
    return output


def window_oracle(record, case):
    # Recompute by enumerating positions from the INSERT data, independently of build_tests.py.
    parts = defaultdict(list)
    index = 2 if case["input_type"] == "v_dec" else 3
    for row in record["tables"]["wf_c296_values"]:
        parts[row[0]].append((row[1],row[index]))
    frame = case["family"]
    clauses = {"following":"ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING",
               "current":"ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING",
               "bounded":"ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING",
               "cumulative":"ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW"}
    assert clauses[frame] in record["ast"].sql(dialect="mysql").upper()
    assert record["ast"].find(exp.Avg).this.name == case["input_type"]
    output = []
    for group,part in sorted(parts.items()):
        part.sort()
        for p,(ident,_) in enumerate(part):
            eligible = []
            for j,(_,value) in enumerate(part):
                keep = {"following": j>p, "current": j>=p,
                        "bounded": abs(j-p)<=1, "cumulative": j<=p}[frame]
                if keep:
                    eligible.append(value)
            nonnull = [Decimal(v) for v in eligible if v is not None]
            average = str((sum(nonnull)/Decimal(len(nonnull))).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)) if nonnull else None
            row = [group,ident,average]
            if len(case["columns"]) == 6:
                row += [eligible[0] if eligible else None,eligible[-1] if eligible else None,
                        eligible[1] if len(eligible)>1 else None]
            output.append(row)
    return output


def main():
    manifest = json.loads(read("generation_manifest.json"))
    result = {"database_executed":False,"sqlglot_version":sqlglot.__version__,"targets":[],
              "limitations":["Static dialect parsing is not MySQL server acceptance or optimizer coverage.",
                             "PREPARE/EXECUTE/DEALLOCATE are validated as control syntax and binding lifecycle; inner SELECTs are parsed separately.",
                             "Oracle checks enumerate supplied data under the stated SQL semantics; no observed database result exists."]}
    for target in manifest["targets"]:
        for key in ("src2req_input","src2req_output","req2test_input","req2test_output","sql","expected"):
            assert digest(target[key]) == target[f"{key}_sha256"], key
        stage2 = read(target["req2test_input"])
        assert stage2.count("### Current task") == 1
        assert read(target["src2req_output"]).strip() in stage2.split("### Current task")[1]
        sql = read(target["sql"])
        extracted = re.findall(r"```sql\n(.*?)\n```",read(target["req2test_output"]),re.S)
        assert len(extracted) == 1 and extracted[0] == sql.strip()
        assert "{{" not in stage2 and "{{" not in sql
        records, types, controls = inspect_sql(sql)
        expected = json.loads(read(target["expected"]))["cases"]
        assert [r["label"] for r in records] == [c["case_id"] for c in expected]
        assert len({r["label"] for r in records}) == len(records)
        for record,case in zip(records,expected):
            assert record["ast"].named_selects == case["columns"],case["case_id"]
            if target["target"].startswith("derived_"):
                assert record["settings"]["pushdown"] == case["pushdown"]
                derived = charset_oracle(record)
            elif target["target"].startswith("item_"):
                derived = property_oracle(record)
            else:
                assert record["settings"]["high_precision"] == case["high_precision"]
                derived = window_oracle(record,case)
            assert derived == case["rows"], (case["case_id"],derived,case["rows"])
        result["targets"].append({"target":target["target"],"case_count":len(records),
                                  "parsed_statement_types":types,"separately_checked_controls":controls,
                                  "prompt_lineage":"pass","response_sql_identity":"pass",
                                  "expected_rows_from_inserted_data":"pass"})
    result["status"] = "pass"
    result["data_result_sets"] = sum(t["case_count"] for t in result["targets"])
    (ROOT/"validation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"PASS: {len(result['targets'])} prompt chains; {result['data_result_sets']} result sets; SQL parsing and independent semantic expected-row checks")


if __name__ == "__main__":
    main()
