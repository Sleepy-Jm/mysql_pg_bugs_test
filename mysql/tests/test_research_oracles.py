import unittest
from pathlib import Path
import research_oracles as o

def fixture(rid,bug=False):
    c=o.CASES[rid];v=c['target_versions'][0]
    source=(o.ROOT/'reviewed_cases'/rid/'reproducer.sql').read_text(encoding='utf-8')
    probes=(o.ROOT/'reviewed_cases'/rid/'validation.sql').read_text(encoding='utf-8')
    sql='USE `owned`;\nSET time_zone="+00:00";\n'+o.PREFLIGHT_SQL+';\n'+source+'\n'+probes
    vals=c['oracle']['reported_result_sets'] if bug else c['oracle']['normal_result_sets']
    if rid=='110003' and not bug:vals=[[],[['8']],[['0']],[['8']]]
    if rid=='113180' and not bug:vals=[[],[['1','0']]]
    checks=c['oracle']['validation_expected']
    if rid=='110003':checks=[[['8']]]
    if rid=='111429':checks=[[[str(i),f'{1994+i}-03-04 12:20:00.000000',(['616161'+'00'*8,'626262'+'00'*8][i-1] if i<3 else 'NULL')] for i in range(1,6)]]
    if rid=='113180':checks=[[['1','0','0.123','0']]]
    headers=o.HEADERS[rid]+o.PROBE_HEADERS[rid]
    outputs=list(zip(headers,vals+checks)); chunks=[];i=0
    for n,s in enumerate(o.split_sql(sql)):
        if n==0:continue
        body=''
        if n==2:body='\t'.join(o.PREFLIGHT_HEADERS)+'\n'+'\t'.join(['STRICT_TRANS_TABLES','utf8mb4','utf8mb4','utf8mb4_0900_ai_ci','+00:00','4','1','1'])
        elif n>2 and s['normalized'].startswith(('select','values','show')):
            h,rows=outputs[i];i+=1
            if rows:body='\t'.join(h)+'\n'+'\n'.join('\t'.join(r) for r in rows)
        if rid=='110125' and s['normalized'].startswith('insert'):body+='\nWarning (Code 1681): DELAYED ignored'
        chunks.append('--------------\n'+s['sql']+'\n--------------\n'+body+'\n')
    record={'sql_submitted':True,'requested_version':v,'target_version':v,'actual_version':v,'isolated_database':'owned','returncode':0,'log_capture_returncode':0}
    env={'actual_version':v,'build_type':'release','network':'none','published_ports':[],'variables':{'version':v,'default_storage_engine':'InnoDB'}}
    return ''.join(chunks),'',sql,record,env

class OracleTest(unittest.TestCase):
    def test_all_normal(self):
        for rid in o.CASES:
            with self.subTest(rid=rid):self.assertEqual(o.evaluate(rid,*fixture(rid))['category'],'not_reproduced')
    def test_all_reported(self):
        for rid in o.CASES:
            with self.subTest(rid=rid):self.assertEqual(o.evaluate(rid,*fixture(rid,True))['category'],'reproduced')
    def test_missing_cast_probe(self):
        args=list(fixture('112910',True));args[0]=args[0].replace('0.0625\t4','0.0624\t4')
        self.assertEqual(o.evaluate('112910',*args)['category'],'inconclusive')
    def test_hex_padded_bit(self):
        args=list(fixture('110003',True));args[0]=args[0].replace('123\t1\n','123\t01\n')
        self.assertEqual(o.evaluate('110003',*args)['category'],'reproduced')
    def test_missing_verbose_stage(self):
        args=list(fixture('112439',True));args[0]=args[0][args[0].find('--------------',15):]
        self.assertEqual(o.evaluate('112439',*args)['category'],'inconclusive')
    def test_sql_error_stage(self):
        args=list(fixture('112439',True));args[1]='ERROR 1064 (42000) at line 6: bad syntax\n';args[3]['returncode']=1
        r=o.evaluate('112439',*args);self.assertEqual(r['category'],'execution_failed');self.assertEqual(r['errors'][0]['code'],1064)
    def test_wrong_version(self):
        args=list(fixture('112439'));args[3]['actual_version']='8.0.35'
        self.assertEqual(o.evaluate('112439',*args)['category'],'inconclusive')
    def test_other_anomaly(self):
        args=list(fixture('112439',True));args[0]=args[0].replace('i\n1\n2\n3\n','i\n1\n2\n4\n',1)
        self.assertEqual(o.evaluate('112439',*args)['category'],'other_anomaly')
    def test_timeout(self):
        args=list(fixture('112439',True));args[3]['timed_out']=True
        self.assertEqual(o.evaluate('112439',*args)['category'],'execution_failed')
    def test_not_executed(self):
        self.assertEqual(o.evaluate('112439','','','',{'sql_submitted':False,'execution_status':'not_scheduled'},{})['category'],'not_executed')
    def test_environment_blocked(self):
        self.assertEqual(o.evaluate('112439','','','',{'sql_submitted':False,'execution_status':'blocked','blocked_reason':'engine initialization failed'},{})['category'],'execution_failed')

if __name__=='__main__':unittest.main()
