from pathlib import Path
import sys,unittest
r=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(r/'src'/'mysql_bugs_test'))
sys.path.insert(0,str(r/'tests'))
s=unittest.defaultTestLoader.discover(str(r/'tests'))
raise SystemExit(not unittest.TextTestRunner(verbosity=2).run(s).wasSuccessful())
