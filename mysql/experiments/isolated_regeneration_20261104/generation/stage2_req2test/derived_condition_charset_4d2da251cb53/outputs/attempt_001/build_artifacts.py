
import json, hashlib, pathlib, platform, sys
from fractions import Fraction
from decimal import Decimal, localcontext, ROUND_HALF_UP
ROOT = pathlib.Path(__file__).resolve().parent
TARGET = ROOT.parent.parent.name
BASE = ROOT.parent.parent
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def put(name, value):
    p=ROOT/name
    if p.exists(): raise RuntimeError("Refusing overwrite: "+str(p))
    p.write_text(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
a=json.loads((BASE/"allowlist.json").read_text(encoding="utf-8-sig"))
assert a["target_id"]==TARGET and a["stage"]=="req2test"
assert a["attempt_id"]=="attempt_001"
assert a["experiment_id"]==a["run_id"]=="mysql_three_isolated_regeneration_20261104"
assert pathlib.Path(a["workspace_root"]).resolve()==BASE
assert pathlib.Path(a["write_root"]).resolve()==ROOT
for f in a["read_files"]:
    p=pathlib.Path(f["path"])
    assert p.is_absolute() and p.resolve().is_relative_to(BASE) and not p.is_symlink()
    assert sha(p)==f["sha256"]
h=json.loads(next(pathlib.Path(f["path"]) for f in a["read_files"] if f["role"]=="handoff_manifest").read_text(encoding="utf-8-sig"))
assert h["ready"] is True and h["requirements_status"]=="ready" and h["exposure_status"]=="no_observed_violation"
for k in ("experiment_id","run_id","target_id"): assert h[k]==a[k]
assert h["to_stage"]=="req2test" and h["to_attempt_id"]==a["attempt_id"]
req=next(f for f in a["read_files"] if f["role"]=="requirements")
assert h["requirements"]=={"path":req["path"],"sha256":req["sha256"]}
status={"database_executed":False,"coverage_status":"not_measured","reproduction_status":"unknown"}
def finish(state,files,checks):
    for name in files:
        if name.endswith(".json"): json.loads((ROOT/name).read_text(encoding="utf-8"))
    manifest={
      "schema_version":1,**{k:a[k] for k in ("experiment_id","run_id","attempt_id","target_id","stage","workspace_root","write_root")},
      "evaluation_mode":"isolated_regeneration","counts_as_unknown_defect_discovery":False,
      "generation_status":state,**status,
      "inputs":[{**f,"actual_sha256":sha(f["path"])} for f in a["read_files"]],
      "controls":[{"path":str(BASE/"allowlist.json"),"sha256":sha(BASE/"allowlist.json")},
                  {"path":str(BASE/"req2test_start.txt"),"sha256":sha(BASE/"req2test_start.txt")}],
      "startup_prompt_sha256":sha(BASE/"req2test_start.txt"),
      "outputs":[{"path":str(ROOT/n),"sha256":sha(ROOT/n)} for n in ["build_artifacts.py"]+files],
      "manifest_self_hash_included":False,
      "environment":{"os":platform.platform(),"python":sys.version,"model":"GPT-6 (system identity)","model_variant":"unknown","sampling_configuration":"unknown","mysql_version":"unknown","mysql_connection_count":0,"shell":"PowerShell"},
      "actual_commands":[{"command":"python '"+str(ROOT/"build_artifacts.py")+"'","purpose":"standard-library artifact writing and independent frame arithmetic; no database calls"},
        {"tool_call":"ec3ddb","purpose":"explicit path/link metadata, output existence and startup prompt hashes"},
        {"tool_call":"b714e2","purpose":"verify current attempt directories empty; metadata only"}],
      "command_log_note":"Input reads/hash-check commands and script-deployment command are in coordinator-retained tool transcript. This manifest and stage2_response.txt are not complete conversation logs.",
      "extra_context":["Platform cwd initially stage1_src2req; no files there read, later commands explicitly use stage2_req2test.","User attachment contains all three target instructions; targets share this chat.","Initial nonrecursive listing of stage2 root exposed three target directory names and START_req2test.txt metadata only before allowlist.","Host/system/developer tool and skill catalogs visible; no skill files, network, source, Git or other chats read.","All three groups were read in specified target order with full example before each handoff/requirements; outputs finalized subsequently in same order."],
      "boundary_audit":{"observed_forbidden_content_exposure":False,"initial_metadata_discovery_deviation":"Nonrecursive root metadata listing preceded allowlist. No input contents or answers exposed. Recorded without claiming absolute absence of contamination.","external_links_followed":False,"database_invoked":False,"network_used":False,"other_attempts_read":False,"inputs_modified":False},
      "static_checks":checks+["allowlist identities, declared paths and all input SHA256 checked","handoff identity/path/hash and required statuses checked","JSON roundtrip parsed","exclusive creation; existing attempts not overwritten"],
      "static_checks_are_database_tests":False,"example_overlap":"Allowed materials show no same repair or substantially same trigger as INTERSECT/EXCEPT example.",
      "freeze_policy":"No subsequent modification in this attempt; execution feedback or supplemental requirements require new attempt."
    }
    put("generation_manifest.json",manifest)
    print(json.dumps({"target":TARGET,"status":state,"files":len(files)+2,**status}))

blocked=[
 {"candidate_id":"C1","requirements":["R1","R2","R3","R4","R5"],"reason":"Frozen requirements explicitly leave target-version character set/collation syntax and nonmerge control to stage B validation. No verified setting/method or precise parsing/conversion prerequisites are supplied; target-specific validation is disallowed here. Cannot assert a complete executable setup by inventing switches.",
  "questions":["Supply target-version-supported nonmerge method and exact downpush eligibility setting with its verified syntax; distinguish prerequisites from unmeasured branch reachability.","Supply a supported charset/collation pair and exact non-ASCII byte/character input syntax plus conversion semantics under the selected connection settings."]},
 {"candidate_id":"C2","requirements":["R3","R4","R5"],"reason":"Depends on stable C1. No validated explicit/implicit introducer encoding and same/different connection-charset configurations are frozen.","questions":["Specify byte encodings, literal declaration and connection/client/result charset settings for representable non-ASCII and ASCII controls; document expected conversions."]},
 {"candidate_id":"C3","requirements":["R1","R2","R3"],"reason":"Depends on C1; no version-validated enabled/disabled pushdown configuration or agreed blocking-form control has been established.","questions":["Supply exact control syntax or approve a specific LIMIT-based blocker with unchanged mathematical rows; freeze via a new attempt."]}
]
put("requirement_mapping.json",{"cases":[],"blocked_candidates":blocked,"not_selected_candidates":[]})
put("oracle.md","""本组全部候选 blocked，未生成 test.sql 或 expected.json。
阻塞来自冻结需求未提供并要求按目标版本验证的可执行前提，不是断言存在缺陷，也不把未测覆盖本身当作 SQL 不合法的证据。
补充材料须由协调者在新 attempt 冻结；本阶段不查源码、网络或阶段一目录代补。
没有固定合法编码/转换配置，无法逐项给出非 ASCII 字符、字节和比较真值，故不伪造独立 oracle。

覆盖观察计划（仅转述需求）
R1：记录下推门槛；R2：记录 derived_table/table_ref、field_index 与克隆对象；R3：记录打印标志、字节、parse_sql 结果；R4/R5：记录 is_cs_specified、collation、缓冲区和解析端字符集，分别确认 introducer 分支。EXPLAIN 仅为线索；未确认可达。

database_executed=false
coverage_status=not_measured
reproduction_status=unknown
""")
put("stage2_response.txt","""derived_condition_charset_4d2da251cb53 / attempt_001
状态：blocked。白名单身份、三个输入 SHA256、交接 ready/status/path/hash 均通过；已完整读取本组 INTERSECT 示例后读取交接与需求。
C1-C3 的阻塞问题及待补充项保存在 requirement_mapping.json。目标版本的字符集/转换及防合并/下推控制前提尚需协调者核验并以新 attempt 交接。本次没有生成 test.sql 或 expected.json。
oracle.md 保存不生成 oracle 的原因及独立覆盖观察计划。
未执行数据库，覆盖未测量，复现未知。不计入未知缺陷发现率。三组共享本聊天；初次白名单前的根目录元数据列举已在清单记录，未读取禁读文件内容。本回答文件不是完整对话日志。
""")
finish("blocked",["requirement_mapping.json","oracle.md","stage2_response.txt"],["All C1-C3 retained as blocked; no SQL or expected-result files fabricated"])
