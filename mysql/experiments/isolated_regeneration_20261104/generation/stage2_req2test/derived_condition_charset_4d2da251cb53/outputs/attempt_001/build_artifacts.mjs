
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url)),base=path.dirname(path.dirname(root));
const sha=async p=>crypto.createHash('sha256').update(await fs.readFile(p)).digest('hex');
const put=async(n,v)=>fs.writeFile(path.join(root,n),typeof v==='string'?v:JSON.stringify(v,null,2)+'\n',{encoding:'utf8',flag:'wx'});
const a=JSON.parse(await fs.readFile(path.join(base,'allowlist.json'),'utf8'));
if(a.target_id!==path.basename(base)||a.stage!=='req2test'||a.attempt_id!=='attempt_001'||a.experiment_id!==a.run_id||a.run_id!=='mysql_three_isolated_regeneration_20261104'||path.resolve(a.workspace_root)!==base||path.resolve(a.write_root)!==root)throw Error('identity');
for(const f of a.read_files){if(!path.isAbsolute(f.path)||!path.resolve(f.path).startsWith(base+path.sep)||await sha(f.path)!==f.sha256)throw Error('input');}
const hf=a.read_files.find(f=>f.role==='handoff_manifest'),req=a.read_files.find(f=>f.role==='requirements');
const h=JSON.parse(await fs.readFile(hf.path,'utf8'));
if(h.ready!==true||h.requirements_status!=='ready'||h.exposure_status!=='no_observed_violation'||h.to_stage!=='req2test'||h.to_attempt_id!==a.attempt_id||h.requirements.path!==req.path||h.requirements.sha256!==req.sha256)throw Error('handoff');
for(const k of ['experiment_id','run_id','target_id'])if(a[k]!==h[k])throw Error('handoff identity');
const files={"requirement_mapping.json":{"cases":[],"blocked_candidates":[{"candidate_id":"C1","requirements":["R1","R2","R3","R4","R5"],"reason":"Frozen requirements leave version-specific charset/collation, conversion and nonmerge/control validation to stage B. No validated prerequisites are supplied; this stage cannot execute a target parser, browse or consult source.","questions":["Supply target-validated nonmerge method and pushdown eligibility control syntax.","Supply supported charset/collation, exact non-ASCII byte input syntax and connection/conversion prerequisites via a new attempt."]},{"candidate_id":"C2","requirements":["R3","R4","R5"],"reason":"Depends on C1. Exact introducer/implicit-literal bytes and same/different connection charset configurations are not validated.","questions":["Freeze representable non-ASCII and ASCII inputs, byte encodings and conversion/comparison semantics in new attempt."]},{"candidate_id":"C3","requirements":["R1","R2","R3"],"reason":"Depends on C1. No version-validated disabled-pushdown or agreed blocker control established.","questions":["Freeze control syntax or a specific LIMIT blocker that preserves mathematical rows."]}],"not_selected_candidates":[]},"oracle.md":"本组全部候选 blocked，未生成 test.sql 或 expected.json。\n阻塞来自冻结需求未提供并要求按目标版本验证的可执行前提，不是断言存在缺陷，也不把未测覆盖本身当作 SQL 不合法的证据。\n补充材料须由协调者在新 attempt 冻结；本阶段不查源码、网络或阶段一目录代补。\n没有固定合法编码/转换配置，无法逐项给出非 ASCII 字符、字节和比较真值，故不伪造独立 oracle。\n\n覆盖观察计划（仅转述需求）\nR1：记录下推门槛；R2：记录 derived_table/table_ref、field_index 与克隆对象；R3：记录打印标志、字节、parse_sql 结果；R4/R5：记录 is_cs_specified、collation、缓冲区和解析端字符集，分别确认 introducer 分支。EXPLAIN 仅为线索；未确认可达。\n\ndatabase_executed=false\ncoverage_status=not_measured\nreproduction_status=unknown\n","stage2_response.txt":"derived_condition_charset_4d2da251cb53 / attempt_001\n状态：blocked。白名单身份、三个输入 SHA256、交接 ready/status/path/hash 均通过；已完整读取本组 INTERSECT 示例后读取交接与需求。\nC1-C3 的阻塞问题及待补充项保存在 requirement_mapping.json。目标版本的字符集/转换及防合并/下推控制前提尚需协调者核验并以新 attempt 交接。本次没有生成 test.sql 或 expected.json。\noracle.md 保存不生成 oracle 的原因及独立覆盖观察计划。\n未执行数据库，覆盖未测量，复现未知。不计入未知缺陷发现率。三组共享本聊天；初次白名单前的根目录元数据列举已在清单记录，未读取禁读文件内容。本回答文件不是完整对话日志。\n"};
for(const [name,value] of Object.entries(files))await put(name,value);
const checks=['input identity/path/SHA256 and handoff statuses matched','JSON outputs parsed before serialization','exclusive file creation'];
if(files['expected.json']){
 const ids=files['expected.json'].cases.map(c=>c.case_id);
 if(new Set(ids).size!==ids.length)throw Error('duplicate case');
 if(files['requirement_mapping.json'].cases.length!==ids.length)throw Error('mapping');
 for(const id of ids)if(files['test.sql'].split('-- case_id '+id+';').length!==2)throw Error('SQL marker');
 checks.push(ids.length+' unique case markers match expected and mapping');
}


const names=['build_artifacts.mjs',...Object.keys(files),'build_artifacts.py'];
const outputs=[];for(const n of names)outputs.push({path:path.join(root,n),sha256:await sha(path.join(root,n))});
const controls=[];for(const n of ['allowlist.json','req2test_start.txt'])controls.push({path:path.join(base,n),sha256:await sha(path.join(base,n))});
const manifest={
 schema_version:1,...Object.fromEntries(['experiment_id','run_id','attempt_id','target_id','stage','workspace_root','write_root'].map(k=>[k,a[k]])),
 generation_status:'blocked',evaluation_mode:'isolated_regeneration',counts_as_unknown_defect_discovery:false,
 database_executed:false,coverage_status:'not_measured',reproduction_status:'unknown',
 inputs:await Promise.all(a.read_files.map(async f=>({...f,actual_sha256:await sha(f.path)}))),controls,startup_prompt_sha256:controls[1].sha256,outputs,manifest_self_hash_included:false,
 environment:{os:os.platform()+' '+os.release(),node:process.version,shell:'PowerShell',model:'GPT-6 (system identity)',exact_model_variant:'unknown',sampling_configuration:'unknown',mysql_version:'unknown',mysql_connections:0,python:'unavailable (py reported No installed Python found)'},
 actual_commands:[{command:'node "'+path.join(root,'build_artifacts.mjs')+'"',purpose:'exclusive artifact creation, standard-library arithmetic/static verification and hashing'},
 
 {tool_calls:['ec3ddb','b714e2'],purpose:'explicit directory/link metadata and empty attempt checks'},
 {command:'python "<USER_HOME>\\Desktop\\mysql_bug_test\\stage2_req2test\\derived_condition_charset_4d2da251cb53\\outputs\\attempt_001\\build_artifacts.py"',result:'exit 1, no output; no artifacts produced'},
 {command:'py --version',result:'No installed Python found; exit 1'},
 {command:'Get-Command node -ErrorAction SilentlyContinue | Select-Object Name,Source | ConvertTo-Json -Compress',result:'C:\\Program Files\\nodejs\\node.exe'}],
 command_log_note:'Complete exact read/hash/deployment commands are in coordinator-retained tool transcript. This file is not a complete transcript.',
 failed_attempts:['Initial functions JavaScript btoa unavailable before any file write','Combined script deployment rejected by Windows command-length limit before file creation','Python launcher unavailable; first-group .py retained as unexecuted provenance; no database invoked'],
 extra_context:['Platform initially supplied stage1_src2req cwd; no stage1 files read. All later commands explicitly use stage2_req2test.','All three target startup instructions and subsequent requirements share this chat. Not fully isolated across targets.','Before first allowlist, nonrecursive stage2 root listing exposed three target directory names and START_req2test.txt metadata only.','Platform tool/skill catalogs and host metadata provided automatically. No skill files, source, old answers, network, Git or other conversations read.','Groups read in target order, each full example before current handoff/requirements. Output finalization followed in same target order.'],
 boundary_audit:{forbidden_content_exposure_observed:false,metadata_deviation:'Initial stage2 root metadata listing preceded allowlist; recorded, no forbidden content read.',network:false,database:false,other_attempts_read:false,inputs_modified:false,absolute_contamination_free_claim:false},
 example_overlap:'Allowed evidence does not show same repair or substantially same trigger as INTERSECT/EXCEPT example.',
 static_checks:checks,static_checks_are_database_tests:false,
 unexecuted_source_artifact:'build_artifacts.py was saved before discovering no Python interpreter; retained and hashed, not used to compute or generate final reports.',
 freeze_policy:'No modification after this manifest is saved; execution observations or supplemented prerequisites require a new attempt.'
};
await put('generation_manifest.json',manifest);
console.log(JSON.stringify({target:a.target_id,status:manifest.generation_status,files:outputs.length+1,database_executed:false,coverage_status:'not_measured',reproduction_status:'unknown'}));
