# coding:utf-8
__author__ = 'wyx'
from util import HTMLTestRunner as HTMLTestRunner
import unittest

from config.globalparameter import test_case_path, report_name

'''
构建测试套件，并执行测试
'''


# 构建测试集,包含testcase目录下的以test_login.py文件
suite1 = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test_search.py')

# su = unittest.load_tests()
# 执行测试
if __name__ == "__main__":
    report = report_name + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'自动化测试报告',
        description=u'项目描述:_____'
    )
    runner.run(suite1)
    fb.close()
    # 发送邮件,注释掉注释正常发送邮件
    # time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    # email = send_email.send_email()
    # email.sendReport()