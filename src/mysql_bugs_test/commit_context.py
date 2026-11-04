"""Revision-bound source discovery; lexical hints are not a C++ semantic proof."""
from copy import deepcopy
import hashlib
from pathlib import PurePosixPath
import re
import subprocess

EXTENSIONS = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx", ".yy", ".y", ".l"}
EXCLUDED = {"mysql-test", "test", "tests", "unittest", "unittests", "gunit", ".git", ".secrets"}
KINDS = {"definition", "callers", "source_range", "unknown"}
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(.*)$", re.M)
TOKEN = re.compile(r"(?P<name>[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*)\s*\(")
CONTROL = {"if", "for", "while", "switch", "catch", "sizeof", "alignof", "decltype", "static_assert", "noexcept"}


def git(repo, *args, allow_missing=False):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, encoding="utf-8")
    if result.returncode and not (allow_missing and result.returncode == 1):
        raise ValueError("Git source read failed: " + result.stderr.strip())
    return result.stdout


def source_path(path):
    if not isinstance(path, str) or not path or "\\" in path:
        return False
    p = PurePosixPath(path)
    return (not p.is_absolute() and ".." not in p.parts and not path.startswith("-")
            and p.suffix.lower() in EXTENSIONS and not any(part.lower() in EXCLUDED for part in p.parts))


def mask(text):
    """Preserve offsets/newlines while masking comments and ordinary literals."""
    pattern = r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\''
    return re.sub(pattern, lambda m: "".join("\n" if c == "\n" else " " for c in m.group()), text)


def close_pair(text, start, opening, closing):
    depth = 0
    for i in range(start, len(text)):
        if text[i] == opening:
            depth += 1
        elif text[i] == closing:
            depth -= 1
            if depth == 0:
                return i
    return None


def functions(text):
    """Best-effort named function definitions, including common multiline signatures."""
    clean = mask(text)
    result = []
    last_end = -1
    for match in TOKEN.finditer(clean):
        if match.start() <= last_end or match["name"] in CONTROL:
            continue
        end_args = close_pair(clean, match.end() - 1, "(", ")")
        if end_args is None:
            continue
        tail = re.match(r"\s*(?:(?:const|override|final|noexcept)\s*)*(?:->\s*[\w:<>,*& ]+)?\s*\{", clean[end_args + 1:])
        if not tail:
            continue
        brace = end_args + 1 + tail.end() - 1
        end = close_pair(clean, brace, "{", "}")
        if end is None:
            continue
        start_line = clean.count("\n", 0, match.start()) + 1
        # Include immediately preceding return-type lines, not preceding functions.
        lines = clean.splitlines()
        while start_line > 1 and match.start() > 0:
            previous = lines[start_line - 2].strip()
            if not previous or any(c in previous for c in ";{}#") or "(" in previous:
                break
            start_line -= 1
        result.append(dict(name=match["name"], start_line=start_line,
                           body_start_line=clean.count("\n", 0, brace) + 1,
                           end_line=clean.count("\n", 0, end) + 1, resolution="lexical_candidate"))
        last_end = end
    return result


def module_hint(path):
    rules = [
        ("storage/innobase/", "innodb"), ("sql/auth/", "authentication"),
        ("sql/iterators/window", "window_execution"), ("sql/window", "window_execution"),
        ("sql/opt_", "optimizer"), ("sql/sql_optimizer", "optimizer"),
        ("sql/sql_planner", "optimizer"), ("sql/partition", "partitioning"),
        ("sql/item", "expressions_and_aggregation"), ("sql/sql_parse", "parser"),
        ("sql/sql_yacc", "parser"), ("sql/sql_table", "ddl"),
        ("sql/handler", "storage_interface"), ("sql/rpl", "replication"),
        ("sql/binlog", "replication"), ("mysys/", "runtime"), ("sql/", "sql_server")]
    return {"value": next((v for prefix, v in rules if path.startswith(prefix)), "unknown"),
            "basis": "path_rule", "evidence_path": path, "certainty": "heuristic"}


def ranges(patch):
    return [dict(before={"start_line": int(m[1]), "line_count": int(m[2] if m[2] is not None else 1)},
                 after={"start_line": int(m[3]), "line_count": int(m[4] if m[4] is not None else 1)},
                 header_context=m[5].strip()) for m in HUNK.finditer(patch)]


def classify_change(status, patch):
    hints = []
    changed = "\n".join(line[1:] for line in patch.splitlines()
                        if line.startswith(("+", "-")) and not line.startswith(("+++", "---")))
    for name, expression in (("branch_condition", r"\b(if|switch|while)\s*\("),
                             ("return_expression", r"\breturn\b"), ("call_or_signature", r"\b\w+\s*\("),
                             ("literal_or_constant", r"\b\d+\b")):
        if re.search(expression, changed):
            hints.append(name)
    return {"file_operation": {"A": "added", "D": "deleted", "M": "modified"}.get(status, "unknown"),
            "syntax_hints": hints, "semantic_change_type": "unknown",
            "basis": "git_file_status_and_changed_text", "certainty": "syntax_hints_only"}


def context_range(text, start, end, limit=240):
    lines = text.splitlines(keepends=True)
    if not lines:
        return None, [], False
    matches = [f for f in functions(text) if f["start_line"] <= end and f["end_line"] >= start]
    first = min([max(1, start - 20)] + [f["start_line"] for f in matches])
    last = max([min(len(lines), end + 20)] + [f["end_line"] for f in matches])
    truncated = last - first + 1 > limit
    if truncated:
        # Keep the changed/queried region, even when a large function starts far away.
        first = max(1, start - min(20, limit // 4))
        last = min(len(lines), first + limit - 1)
    return [first, last], matches, truncated


def discover(repo, revision, parent):
    """Exact file/hunk positions plus explicitly heuristic function/module hints."""
    names = git(repo, "diff", "--no-renames", "--name-status", "-z", parent, revision, "--").split("\0")
    changed = [(names[i], names[i + 1]) for i in range(0, len(names) - 1, 2)]
    metadata, entries, excluded = [], [], []
    for status, path in changed:
        if not source_path(path):
            excluded.append({"path": path, "reason": "outside_production_source_policy"})
            continue
        patch = git(repo, "diff", "--no-renames", "--no-ext-diff", "--no-textconv", "--unified=0",
                    parent, revision, "--", path)
        hunks = ranges(patch)
        by_side, related, limitations = {"before": [], "after": []}, [], []
        for side, rev in (("before", parent), ("after", revision)):
            if (status == "A" and side == "before") or (status == "D" and side == "after"):
                continue
            text = git(repo, "show", f"{rev}:{path}")
            for h in hunks:
                loc = h[side]
                if not loc["line_count"]:
                    continue
                start = loc["start_line"]
                span, found, clipped = context_range(text, start, start + loc["line_count"] - 1)
                if span and span not in by_side[side]:
                    by_side[side].append(span)
                for f in found:
                    record = dict(f, side=side, revision=rev)
                    if record not in related:
                        related.append(record)
                if clipped:
                    limitations.append({"side": side, "reason": "context_line_limit", "changed_range": loc})
        metadata.append(dict(path=path, status=status, modification_locations=hunks,
                             change_type=classify_change(status, patch), database_module=module_hint(path),
                             related_functions=related, function_resolution="lexical_candidates" if related else "unknown",
                             limitations=limitations))
        entries.append(dict(path=path, role="production", functions=sorted({f["name"] for f in related}) or ["unknown"],
                            **by_side))
    return {"files": metadata, "excluded_files": excluded, "method": "git_diff_plus_lexical_hints"}, entries


def validate_requests(analysis):
    status = analysis.get("material_status")
    if status not in {"sufficient", "partial", "insufficient"}:
        raise ValueError("material_status must be sufficient, partial, or insufficient")
    requests = analysis.get("missing_materials")
    if not isinstance(requests, list) or (status == "sufficient" and requests) or (status != "sufficient" and not requests):
        raise ValueError("missing_materials must agree with material_status")
    ids = set()
    for request in requests:
        key = request.get("request_id")
        if not isinstance(key, str) or not key.strip() or key in ids:
            raise ValueError("Unique material request_id required")
        ids.add(key)
        if request.get("kind") not in KINDS or request.get("revision") not in {"before", "after", "both"}:
            raise ValueError("Invalid material request kind/revision")
        if any(not isinstance(request.get(k), str) or not request[k].strip() for k in ("needed", "reason")):
            raise ValueError("Describe needed material and why")
        path, symbol = request.get("path"), request.get("symbol")
        if path is not None and not source_path(path):
            raise ValueError("Requested source path is outside production policy")
        if request["kind"] in {"definition", "callers"} and (
                not isinstance(symbol, str) or not re.fullmatch(r"[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*", symbol)):
            raise ValueError("Source symbol required for definition/callers")
        if request["kind"] == "source_range":
            start, end = request.get("start_line"), request.get("end_line")
            if path is None or type(start) is not int or type(end) is not int or not 1 <= start <= end:
                raise ValueError("Explicit path and valid source range required")


def symbol_hits(repo, revision, symbol, path=None):
    leaf = symbol.split("::")[-1]
    specs = [path] if path else [":(glob)**/*" + ext for ext in sorted(EXTENSIONS)]
    if not path:
        specs += [":(exclude,glob)**/" + part + "/**" for part in sorted(EXCLUDED)]
    output = git(repo, "grep", "-n", "-I", "-F", "--no-color", "-e", leaf, revision, "--", *specs, allow_missing=True)
    hits = []
    for line in output.splitlines():
        match = re.match(re.escape(revision) + r":(.+?):(\d+):(.*)", line)
        if match and source_path(match[1]) and re.search(r"\b" + re.escape(leaf) + r"\s*\(", match[3]):
            hits.append((match[1], int(match[2])))
    return hits


def supplement(repo, material, analysis, max_lines=1600, max_fragments=12):
    """Fetch requested source at the same parent/target only; preserve original IDs."""
    validate_requests(analysis)
    enriched = deepcopy(material)
    original_ids = {s["source_id"] for s in enriched["sources"]}
    used_ids = set(original_ids)
    supplied = []
    outcomes = []
    remaining = max_lines
    cache = {}

    def text_at(rev, path):
        key = rev, path
        if key not in cache:
            cache[key] = git(repo, "show", f"{rev}:{path}")
        return cache[key]

    def add(side, rev, path, start, end, request_id, relation):
        nonlocal remaining
        text = text_at(rev, path)
        lines = text.splitlines(keepends=True)
        if start < 1 or end > len(lines):
            raise ValueError("Requested source range does not exist")
        # Already supplied intervals remain evidence, not new retrieval.
        for old in enriched["sources"]:
            if old["kind"] == side and old["revision"] == rev and old["path"] == path:
                stop = old["start_line"] + len(old["content"].splitlines()) - 1
                if old["start_line"] <= start and end <= stop:
                    return old["source_id"], "already_present"
        if remaining <= 0 or len(supplied) >= max_fragments:
            return None, "budget_exhausted"
        actual_end = min(end, start + remaining - 1, start + 399)
        content = "".join(lines[start - 1:actual_end])
        index = len(enriched["sources"]) + 1
        while f"source_{index}" in used_ids:
            index += 1
        sid = f"source_{index}"
        used_ids.add(sid)
        enriched["sources"].append(dict(source_id=sid, kind=side, path=path, revision=rev,
            start_line=start, content=content, content_sha256=hashlib.sha256(content.encode()).hexdigest(),
            retrieval={"request_id": request_id, "relation": relation, "requested_end_line": end,
                       "truncated": actual_end < end}))
        remaining -= actual_end - start + 1
        supplied.append(sid)
        return sid, "partial" if actual_end < end else "supplied"

    for request in analysis["missing_materials"]:
        outcome = {"request_id": request["request_id"], "needed": request["needed"], "reason": request["reason"],
                   "status": "unresolved", "matches": [], "limitations": []}
        for side, rev in (("before", material["parent_revision"]), ("after", material["target_revision"])):
            if request["revision"] not in {"both", side}:
                continue
            try:
                if request["kind"] == "unknown":
                    outcome["limitations"].append("Request has no retrievable source locator")
                    continue
                if request["kind"] == "source_range":
                    sid, state = add(side, rev, request["path"], request["start_line"], request["end_line"],
                                     request["request_id"], "explicit_range")
                    outcome["matches"].append(dict(side=side, source_id=sid, status=state))
                    continue
                hits = symbol_hits(repo, rev, request["symbol"], request.get("path"))
                matches_before = len(outcome["matches"])
                if len(hits) > 60:
                    outcome["limitations"].append(f"{side}: search has {len(hits)} hits; only first 60 inspected")
                seen = set()
                for path, line in hits[:60]:
                    text = text_at(rev, path)
                    defs = functions(text)
                    if request["kind"] == "definition":
                        matches = [f for f in defs if f["name"] == request["symbol"] or (
                            "::" not in request["symbol"] and f["name"].split("::")[-1] == request["symbol"])]
                        spans = [(f["start_line"], f["end_line"], "lexical_definition_candidate") for f in matches]
                    else:
                        # Exclude symbol's own definition; retain lexical call-site candidates.
                        if any(f["name"].split("::")[-1] == request["symbol"].split("::")[-1]
                               and f["start_line"] <= line <= f["body_start_line"] for f in defs):
                            continue
                        span, _, clipped = context_range(text, line, line, limit=400)
                        spans = [(span[0], span[1], "lexical_call_site_candidate")] if span else []
                        if clipped:
                            outcome["limitations"].append(f"{side}:{path}:{line}: caller context clipped")
                    for start, end, relation in spans:
                        key = path, start, end
                        if key in seen:
                            continue
                        seen.add(key)
                        sid, state = add(side, rev, path, start, end, request["request_id"], relation)
                        outcome["matches"].append(dict(side=side, path=path, line=line, source_id=sid,
                                                        status=state, relation=relation))
                        if state == "budget_exhausted":
                            break
                    if remaining <= 0 or len(supplied) >= max_fragments:
                        outcome["limitations"].append("Retrieval budget exhausted; remaining matches uninspected")
                        break
                if not hits:
                    outcome["limitations"].append(f"{side}: symbol not found in allowed source")
                elif len(outcome["matches"]) == matches_before:
                    outcome["limitations"].append(f"{side}: no matching lexical {request['kind']} context identified")
            except ValueError as error:
                outcome["limitations"].append(f"{side}: {error}")
        positive = [m for m in outcome["matches"] if m["source_id"]]
        if positive:
            outcome["status"] = "partial" if outcome["limitations"] or any(m["status"] in {"partial", "budget_exhausted"} for m in outcome["matches"]) else "supplied_for_reanalysis"
        if len(positive) > 1 and request["kind"] != "source_range":
            outcome["limitations"].append("Multiple lexical candidates; symbol resolution is not proven")
        outcomes.append(outcome)
    enriched["supplementation"] = dict(requests=deepcopy(analysis["missing_materials"]), outcomes=outcomes,
        new_source_ids=supplied, max_lines=max_lines, max_fragments=max_fragments,
        revisions_allowed=[material["parent_revision"], material["target_revision"]],
        semantic_sufficiency="requires_stage1_reanalysis")
    enriched["input_boundary"] = material.get("input_boundary", "") + " + requested same-revision production source"
    return enriched
