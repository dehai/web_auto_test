# coding:utf-8
__author__ = 'wyx'
import unittest
from util.HTMLTestRunner import HTMLTestRunner
from config.globalparameter import test_case_path, report_path_sibling

'''
构建测试套件，并执行测试
'''

# 构建测试集,包含testcase目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')

# 执行测试
if __name__ == "__main__":
    report = report_path_sibling + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner(
        stream=fb,
        title=u'自动化测试报告',
        description=u'项目描述:_____'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件,注释掉注释正常发送邮件
    # time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    # email = send_email.send_email()
    # email.sendReport()
