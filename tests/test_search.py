# coding:utf-8


import unittest
from selenium import webdriver
from page.search_page import SearchPage
from page.login_page import LoginPage
import time


class TestSearch(unittest.TestCase):
    """UI自动化搜索"""
    def setUp(self):
        self.url = "https://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.verificationErrors = []
        self.search_page = SearchPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.sp.open(self.url)
        # self.title = u'百度一下，你就知道'
        # self.mylog = log.log()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_search(self):
        """搜索测试关键字,在结果页中包含‘测试’这2个关键字"""
        try:
           # sp = SearchPage(self.driver)
           # sp.open(self.url)
           self.sp.run_case("测试")
           self.sp.click_link()
           assert u'测试' in self.driver.page_source
           #self.assertIn(u'志' in self.driver.page_source)
           #assert_that(self.driver.page_source).contains("志").does_not_contain("测试")
        except Exception as e:
            self.search_page.img_screenshot(u'搜索测试关键字')
            print(e)
            print(u'搜索测试关键字，在结果页中包含‘测试’这2个关键字case错误！')
            # self.mylog.error(u'搜索测试关键字')
            # raise e

    def test_login(self):
        """登录提示语验证：请您输入验证码"""
        try:
           sp = LoginPage(self.driver)
           sp.open(self.url)
           sp.click_link()
           sp.click_username()
           sp.run_case("john200e", "xxxxx")
           self.assertEqual(sp.get_yanzhengma(), "请您输入验证码", msg="验证成功！")
        except :
            self.search_page.img_screenshot(u'登录提示语验证：请您输入验证码')
            print(u'登录提示语验证，请您输入验证码case错误！')
            # self.mylog.error(u'test_search中的提示语验证码')
            # raise e

    def test_searchwu(self):
        """搜索关键字'吴'，结果页包含关键字：1.打开登录页 2.输入关键字 3.点击检索按钮 4.断言结果页是否包含搜索关键字"""
        try:
            # sp = SearchPage(self.driver)
            # sp.open(self.url)
            self.driver.find_element_by_id("kw").send_keys("吴")
            self.driver.find_element_by_id("su").click()
            assert u'吴' in self.driver.page_source
        # assert_that(self.driver.page_source).contains("志").does_not_contain("测试")
        except Exception as e:
            self.sp.img_screenshot("搜索的关键字不存在")
            print(e.args)
            print(u'搜索关键字‘吴’检索结果页包含搜索关键字错误！')



