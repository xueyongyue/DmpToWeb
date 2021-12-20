import unittest
import app,time
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from script.GetTree import GetTree


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(GetTree))


report_file = app.BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# report_file = app.BASE_DIR + "/report/report.html"
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="入库web化项目接口测试报告",description="test")
    runner.run(suite)