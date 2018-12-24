# coding:utf-8

import time
from os import path
from util.file_reader import YamlReader
'''配置全局参数'''

# 项目绝对路径
# project_path = "E:\\pycharm\\python27\\testPO\\"

#  获取项目路径
project_path = path.abspath(path.join(path.dirname(path.realpath(__file__)[0]), '.'))
# print(u'项目路径：' + project_path)

# 获取当前文件所在目录的绝对路径
parentDirPath = path.dirname(path.dirname(path.abspath(__file__)))
# print(u'项目绝对路径：' + parentDirPath)

# 获取上级目录
siblingDirPath = path.abspath(path.dirname(path.dirname(__file__)))
# print(u'获取上级目录路径: ' + siblingDirPath)

# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath + u"\\config\\PageElementLocator.ini"

# 测试用例代码存放路径(用于构建suite,注意该文件夹下的文件都应该以test开头命名)
# test_case_path = project_path + "\\tests"
# print (u'suite路径：' + test_case_path)
test_case_path = siblingDirPath + "\\tests"
# print (u'suite路径:' + test_case_path)

# excel 测试数据文档存放路径
test_data_path = project_path + "\\data\\testData.xlsx"

# # 日志文件存储路径
log_path_sibling = siblingDirPath + "\\log\\"
log_path = log_path_sibling + "\\mylog.log"

# 日志文件存储路径
sibling_log_path = siblingDirPath + "\\log\\mylog.log"
# print (u"日志路径：" + sibling_log_path)

# 驱动程序路径
chromedriver_path = project_path + "\\driver\\chromedriver.exe"
firefox_path = project_path + "\\driver\\geckdriver.exe"
# print (u'驱动路径:' + firefox_path)
# print (u'驱动路径:' + chromedriver_path)

# 测试报告存储路径，并以当前时间作为报告名称前缀
# report_path = project_path + "\\report\\"
# report_name = report_path + time.strftime('%Y%m%d%H%S',time.localtime())
# 获取上级目录，测试报告存储路径，并以当前时间作为报告名称前缀
report_path_sibling = siblingDirPath + "\\report\\"
# print(u'获取上级目录，测试报告存储路径'+ report_path_sibling)
report_name = report_path_sibling + time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 异常截图存储路径，并以当前时间作为图片名称前缀
# img_path = project_path + "\\printscreen\\" + time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 异常截图存储路径，并以当前时间作为图片名称前缀
img_path = siblingDirPath + "\\printscreen\\" + time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置发送测试报告的公共邮箱、用户名和密码
smtp_server = 'smtp.163.com'                                               # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以foxmail这些工具中验证
email_name = "jack329614640@163.com"                                       # 发件人名称
email_password = "W13119830329yx"                                          # 发件人登录密码
email_To = '328133513@qq.com;jack329614640@163.com'                        # 收件人


"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，
# 也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = path.split(path.dirname(path.abspath(__file__)))[0]
CONFIG_FILE = path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = path.join(BASE_PATH, 'data')
DRIVER_PATH = path.join(BASE_PATH, 'drivers')
LOG_PATH = path.join(BASE_PATH, 'log')
REPORT_PATH = path.join(BASE_PATH, 'report')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)






