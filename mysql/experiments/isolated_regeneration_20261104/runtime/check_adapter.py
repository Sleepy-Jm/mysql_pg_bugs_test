import runner as r
import json,re
p=json.loads((r.ROOT/'runtime_plan.json').read_text(encoding='utf-8-sig'))
for j in p['jobs']:
 if not j.get('inputs'): continue
 for name,info in j['inputs'].items(): assert r.sha(r.ROOT/'inputs'/j['target']/name)==info['sha256']
 sql=(r.ROOT/'inputs'/j['target']/'test.sql').read_bytes()
 assert re.findall(rb'-- case_id ([A-Z_]+)',sql)==[x.encode() for x in j['result_set_order']]
 expected=json.loads((r.ROOT/'inputs'/j['target']/'expected.json').read_text(encoding='utf-8-sig'))['cases']
 assert [e['case_id'] for e in expected]==j['result_set_order']
x=r.parse('<?xml version="1.0"?><resultset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><row><field name="p">1</field><field name="id">2</field><field name="a" xsi:nil="true"/></row></resultset>')
e=dict(case_id='WF_BASE',columns=['p','id','a'],rows=[[1,2,None]])
assert not r.differences(x[0],e)
e['rows'][0][2]='0'; assert len(r.differences(x[0],e))==1
e['rows']=[[1,2,'1.000000']]; x[0]['rows']=[['1','2','1']]; assert not r.differences(x[0],e)
x[0]['rows'][0][2]='1.00000000001'; assert r.differences(x[0],e)
e['case_id']='WF_REAL_LOW'; assert not r.differences(x[0],e)
x[0]['rows'][0][0]='1.00000000001'; assert r.differences(x[0],e)
print('PASS: frozen hashes, case ordering, XML NULL, numeric normalization, exact and floating tolerances')
