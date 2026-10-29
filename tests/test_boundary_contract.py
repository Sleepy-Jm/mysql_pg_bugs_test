import hashlib,json,tempfile,unittest
from pathlib import Path
from run_boundary_core import validate_manifest

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        (self.root/'source.sql').write_text('SELECT 1;\n');(self.root/'post.sql').write_text('-- no postcheck\n')
        h=lambda p:hashlib.sha256((self.root/p).read_bytes()).hexdigest()
        self.m={'run_id':'test_boundary','scope_report_ids':['110076'],'scope_task_ids':['mysql-110076-8.0.32'],'image_ids':{'8.0.31':'sha256:'+'1'*64},'cases':[{'case_id':'report_110076','report_id':'110076','sql_file':'source.sql','script_sha256':h('source.sql'),'postcheck_file':'post.sql','postcheck_sha256':h('post.sql'),'runs':[{'run_id':'control_1','task_id':'mysql-110076-8.0.32','requested_version':'8.0.31','target_version':'8.0.32','role':'adjacent_comparison','cohort':'version_boundary','repeat':1}]}]}
    def tearDown(self):self.tmp.cleanup()
    def validate(self):
        p=self.root/'manifest.json';p.write_text(json.dumps(self.m));return validate_manifest(p)
    def test_exact_predecessor_and_target_identity_preserved(self):
        _,rows=self.validate();self.assertEqual(rows[0]['requested_version'],'8.0.31');self.assertEqual(rows[0]['target_version'],'8.0.32')
    def test_target_run_cannot_enter_control_phase(self):
        self.m['cases'][0]['runs'][0]['role']='target'
        with self.assertRaises(ValueError):self.validate()
    def test_skipping_a_release_rejected(self):
        self.m['cases'][0]['runs'][0]['target_version']='8.0.33'
        with self.assertRaises(ValueError):self.validate()
    def test_changed_source_rejected(self):
        (self.root/'source.sql').write_text('SELECT 2;')
        with self.assertRaises(ValueError):self.validate()
    def test_changed_postcheck_rejected(self):
        (self.root/'post.sql').write_text('SELECT 2;')
        with self.assertRaises(ValueError):self.validate()

if __name__=='__main__':unittest.main()
