# coding:utf-8

import unittest
from selenium import webdriver
from page.login_page import LoginPage
import time
import random
from util import log


class TestLogin(unittest.TestCase):
    '''UI自动化登录'''

    def setUp(self):
        self.url = "https://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        #self.verificationErrors = []
        #self.login_page = LoginPage(self.driver, self.url, u'百度一下，你就知道')
        #self.title = u'百度一下，你就知道'
        self.login_page = LoginPage(self.driver)
        self.mylog = log.log()


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        """ 登录 """
        # sp = LoginPage(self.driver)
        sp = self.login_page
        sp.open(self.url)
        sp.click_link()
        sp.click_username()
        sp.run_case("hanxiaobei","xxxxx")
        self.assertEqual(sp.get_yanzhengma(), "请您输入验证码", msg="验证成功！")

    def test_loginEmpty(self):
        '''账号、密码为空登录'''
        try:
           sp = LoginPage(self.driver)
           sp.open(self.url)
           sp.click_link()
           sp.click_username()
           sp.run_case("","")
           self.assertEqual(sp.user_error_hint(),"请您输入手机/邮箱/用户名")
        except Exception as e:
            self.login_page.img_screenshot(u'账号和密码不能为空')
            self.mylog.error(u'账号、密码为空登录：账号和密码不能为空')
            raise e

    def  test_loginEmptyPassword(self):
        '''账号正确、密码为空登录'''
        try:
           sp = LoginPage(self.driver)
           sp.open(self.url)
           sp.click_link()
           sp.click_username()
           sp.run_case("john200e","")
           self.assertEqual(sp.pawd_error_hint(),"请您输入密码",msg="验证成功！")
        except Exception as e:
            self.login_page.img_screenshot(u'请您输入密码')
            self.mylog.error(u'账号正确、密码为空登录：请您输入密码')
            raise e

    def  test_loginEmptyUsername(self):
        '''账号为空、密码不为空'''
        try:
           sp = LoginPage(self.driver)
           sp.open(self.url)
           sp.click_link()
           sp.click_username()
           sp.run_case("","xxxxx")
           self.assertEqual(sp.user_error_hint(),"请您输入手机/邮箱/用户名",msg="验证成功！")
        except Exception as e:
            self.login_page.img_screenshot(u'请您输入手机/邮箱/用户名')
            self.mylog.error(u'账号为空、密码不为空：请您输入手机/邮箱/用户名')
            raise e


    def  test_loginNotVerfication(self):
         '''账号和密码不匹配'''
         try:
             character = random.choice('abcdefghijklmnopqrstuvwxyz')
             username = "john200e" + character
             sp = LoginPage(self.driver)
             sp.open(self.url)
             sp.click_link()
             sp.click_username()
             sp.run_case(value1=username, value2="123456")
             self.assertEqual(sp.pawd_error_hint(), "用户名或密码有误，请重新输入或找回密码",msg="验证成功！")
         except Exception as e:
             self.login_page.img_screenshot(u'用户名或密码有误，请重新输入或找回密码')
             self.mylog.error(u'账号和密码不匹配：用户名或密码有误，请重新输入或找回密码')
             raise e

