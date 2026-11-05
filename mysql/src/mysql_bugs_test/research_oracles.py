"""Six-way offline adjudication for the reviewed ordinary SQL official-version batch."""
from collections import Counter
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
from sql_evidence_parser import split_sql, normalize_sql, parse_verbose, parse_errors

ROOT=Path(__file__).resolve().parents[2] / 'experiments' / 'saved_20261029' / 'official_research_20261029'
SELECTION=json.loads((ROOT/'reviewed_execution_selection.json').read_text(encoding='utf-8'))
CASES={c['report_id']:c for c in SELECTION['selected']}
LABELS={'reproduced':'已复现','not_reproduced':'完整执行但未复现','inconclusive':'条件不足、无法判断',
        'execution_failed':'执行受阻或失败','other_anomaly':'其他异常、待归因','not_executed':'未执行'}
PREFLIGHT_SQL=('SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,'
 '@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,'
 '@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,'
 '@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset')
PREFLIGHT_HEADERS=['__preflight_sql_mode','__preflight_charset_client','__preflight_charset_connection',
 '__preflight_collation','__preflight_time_zone','__preflight_div_precision','__preflight_autoincrement','__preflight_offset']
HEADERS={'107337':[['a']]*4,'110003':[['id','HEX(val)'],['before_count'],['deleted_count'],['after_count']],
 '110125':[['c0']],'110244':[['USER_ID','PAGE_ID']]*2,'110256':[['c0']]*2,
 '111429':[['binary_col','timestamp_col']]*3,'112439':[['i']]*2,'113180':[['c0','c1']]*2,
 '112910':[['column_0','column_1']]*2}
PROBE_HEADERS={'107337':[['loaded_rows','min_a','max_a']],'110003':[['rows_left']],
 '110125':[['loaded_rows','min_value','max_value']],'110244':[['USER1_ID','USER2_ID'],['USER_ID','PAGE_ID'],['PAGE_ID']],
 '110256':[['loaded_rows','min_value','max_value']],'111429':[['id_col','timestamp_col','binary_hex']],
 '112439':[['i']],'113180':[['c0','c1','sin_value','sin_is_null']],
 '112910':[['expected_constant','div_precision']]}
WARNING=re.compile(r'^(?:Warning|Note|Error) \(Code \d+\):')
def multisets(rows):return [Counter(tuple(v) for v in result) for result in rows]
def numeric(v):return Decimal(v)
def clean_segment(seg):
    lines=[x.rstrip('\r') for x in seg['raw_body'].splitlines() if x.strip()]
    warnings=[x for x in lines if WARNING.match(x)]
    lines=[x for x in lines if not WARNING.match(x) and not re.match(r'^(?:Query OK,|Empty set(?:\s|$)|\d+ rows? in set\b|Bye$)',x)]
    header=lines[0].split('\t') if lines else []
    rows=[x.split('\t') for x in lines[1:]]
    return dict(seg,header=header,rows=rows,shape_valid=all(len(x)==len(header) for x in rows),warnings=warnings)

def evaluate(report_id, stdout, stderr, executed_sql, record, environment):
    rid=str(report_id);statements=[];results=[];errors=[];pre={}
    def done(cat,reason):return {'report_id':rid,'category':cat,'label':LABELS[cat],'reason':reason,
        'statements':statements,'resultsets':results,'errors':errors,'preconditions':pre,
        'independent_bug_count':None,'introduction_result':None}
    if not record.get('sql_submitted'):
        reason=record.get('blocked_reason') or record.get('restriction_reason') or record.get('execution_status') or '尚未安排'
        status=record.get('execution_status','')
        return done('execution_failed' if status in ('blocked','failed','initialization_failed','transport_error') else 'not_executed',str(reason))
    if rid not in CASES:return done('inconclusive','Report outside frozen reviewed matrix')
    case=CASES[rid];v=record.get('requested_version');vars=environment.get('variables',{})
    if v not in case['target_versions'] or any(x!=v for x in [record.get('actual_version'),record.get('target_version'),environment.get('actual_version'),vars.get('version')]):
        return done('inconclusive','Requested/actual version mismatch with official Version matrix')
    if environment.get('build_type')!='release' or environment.get('network')!='none' or environment.get('published_ports')!=[]:
        return done('inconclusive','Isolated release environment not established')
    if vars.get('default_storage_engine','').lower()!='innodb':return done('inconclusive','InnoDB precondition absent')
    if record.get('timed_out') or record.get('oom_killed'):return done('execution_failed','Timeout/OOM prevents completed test; not the report phenomenon')
    if record.get('server_crash_evidence') or record.get('assertion_in_log'):return done('other_anomaly','Unexpected server signal in wrong-result case; not attributable to this report')
    if record.get('log_capture_returncode')!=0:return done('execution_failed','Service-log capture failed')
    try:
        statements=split_sql(executed_sql)
        source=split_sql((ROOT/'reviewed_cases'/rid/'reproducer.sql').read_text(encoding='utf-8'))
        probes=split_sql((ROOT/'reviewed_cases'/rid/'validation.sql').read_text(encoding='utf-8'))
        segments=[clean_segment(s) for s in parse_verbose(stdout)]
        errors,unparsed=parse_errors(stderr,statements)
    except (ValueError,TypeError) as exc:return done('inconclusive','Evidence parse failed: '+str(exc))
    if errors or unparsed:
        # All reports in this specific frozen subset target wrong results. Other
        # report families must provide their own mapped expected-error contract.
        return done('execution_failed','Unexpected SQL/client error; see mapped statement_index, SQLSTATE and error code')
    if record.get('returncode')!=0:return done('execution_failed','Client nonzero exit without mapped expected-error contract')
    expected=[s['normalized'] for s in source+probes]
    if len(statements)!=3+len(expected) or [s['normalized'] for s in statements[3:]]!=expected:
        return done('inconclusive','Submitted source/probe SQL or original order differs from reviewed contract')
    if not re.fullmatch(r'use\s+`?[a-zA-Z0-9_]+`?',statements[0]['normalized']):return done('inconclusive','Owned USE prelude absent')
    if record.get('isolated_database') and statements[0]['normalized'].replace('`','')!='use '+record['isolated_database'].lower():return done('inconclusive','Owned schema mismatch')
    if statements[1]['normalized'] not in {'set time_zone="+00:00"',"set time_zone='+00:00'"} or statements[2]['normalized']!=normalize_sql(PREFLIGHT_SQL):
        return done('inconclusive','Session prelude/probe differs from frozen runner')
    if [s['normalized'] for s in segments]==[s['normalized'] for s in statements[1:]]:
        segments=[{'sql':statements[0]['sql'],'normalized':statements[0]['normalized'],'header':[],'rows':[],'shape_valid':True,'warnings':[]}]+segments
        pre['client_USE_omission']=True
    if [s['normalized'] for s in segments]!=[s['normalized'] for s in statements]:return done('inconclusive','Verbose transcript is incomplete or reordered')
    q=segments[2]
    if q['header']!=PREFLIGHT_HEADERS or len(q['rows'])!=1:return done('inconclusive','Actual-session settings not available')
    session=dict(zip(q['header'],q['rows'][0]));pre['actual_session']=session
    if (session['__preflight_charset_client']!='utf8mb4' or session['__preflight_charset_connection']!='utf8mb4' or
        session['__preflight_time_zone']!='+00:00' or session['__preflight_div_precision']!='4' or
        session['__preflight_autoincrement']!='1' or session['__preflight_offset']!='1'):
        return done('inconclusive','Required actual-session setting differs')
    source_results=[s for s in segments[3:3+len(source)] if re.match(r'(?i)^(SELECT|VALUES|SHOW)\b',s['sql'])]
    probe_results=segments[3+len(source):];results=source_results+probe_results
    headers=HEADERS[rid]+PROBE_HEADERS[rid]
    norm=lambda hs:[re.sub(r'\s+','',x).lower() for x in hs]
    if len(results)!=len(headers) or any(not s['shape_valid'] or (s['header'] and norm(s['header'])!=norm(e)) for s,e in zip(results,headers)):
        return done('inconclusive','Result headers or tabular shape differ from submitted query contract')
    rows=[s['rows'] for s in source_results];checks=[s['rows'] for s in probe_results]
    valid=False
    try:
        if rid in ['107337','110244','112439']:
            valid=multisets(checks)==multisets(case['oracle']['validation_expected'])
        elif rid in ['110125','110256']:
            valid=len(checks)==1 and len(checks[0])==1 and [numeric(v) for v in checks[0][0]]==[Decimal(1),Decimal(0),Decimal(0)]
        elif rid=='110003':
            valid=len(checks)==1 and len(checks[0])==1 and len(rows)==4 and rows[1]==[['8']] and checks[0]==rows[3]
        elif rid=='111429':
            expected=[]
            for i in range(1,6):expected.append([str(i),f'{1994+i}-03-04 12:20:00.000000',(['616161'+'00'*8,'626262'+'00'*8][i-1] if i<3 else 'NULL')])
            valid=checks==[expected]
        elif rid=='113180':
            valid=len(checks)==1 and len(checks[0])==1 and len(checks[0][0])==4 and checks[0][0][:2]==['1','0'] and checks[0][0][3]=='0' and numeric(checks[0][0][2]).is_finite()
        elif rid=='112910':valid=len(checks)==1 and len(checks[0])==1 and len(checks[0][0])==2 and numeric(checks[0][0][0])==Decimal('0.0625') and checks[0][0][1]=='4'
    except (InvalidOperation,ValueError,IndexError,TypeError):valid=False
    pre['post_source_validation_passed']=valid
    if not valid:return done('inconclusive','Required same-session data/control validation failed or missing')
    normal=bug=False
    try:
        if rid=='110003':
            before=int(rows[1][0][0]);deleted=int(rows[2][0][0]);after=int(rows[3][0][0])
            selected_expected=(len(rows[0])==1 and len(rows[0][0])==2 and rows[0][0][0]=='123'
                               and re.fullmatch(r'[0-9A-Fa-f]+',rows[0][0][1]) and int(rows[0][0][1],16)==1)
            normal=before==8 and 0<=deleted<=1 and after==before-deleted and len(rows[0])==deleted and (not rows[0] or selected_expected)
            bug=selected_expected and before==8 and deleted==0 and after==8
        elif rid=='113180':
            r=[['1','0']];normal=rows in ([r,[]],[[],r]);bug=rows==[r,r]
        elif rid=='110125':
            normal=rows==[[]];bug=len(rows)==1 and len(rows[0])==1 and len(rows[0][0])==1 and numeric(rows[0][0][0])==0
        else:
            normal=multisets(rows)==multisets(case['oracle']['normal_result_sets'])
            bug=multisets(rows)==multisets(case['oracle']['reported_result_sets'])
    except (ValueError,IndexError,InvalidOperation,TypeError):return done('inconclusive','Cannot interpret required numeric outputs')
    if bug:return done('reproduced','Exact reported wrong-result pattern and all required same-session controls match')
    if normal:return done('not_reproduced','All required steps and controls completed; target phenomenon not observed; 原因未确定')
    return done('other_anomaly','Completed observation differs from both normal contract and report pattern; attribution not established')
