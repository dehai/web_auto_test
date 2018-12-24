# coding:utf-8


from selenium.webdriver.common.by import By
from lib.base_page import Action
import time


class LoginPage(Action):
    link_loc = (By.LINK_TEXT, "登录")
    name_loc = (By.ID, "TANGRAM__PSP_10__userName")
    password_loc = (By.ID, "TANGRAM__PSP_10__password")
    submit_loc = (By.ID, "TANGRAM__PSP_10__submit")
    username_loc = (By.ID, "TANGRAM__PSP_10__footerULoginBtn")
    username_top = (By.LINK_TEXT, "hanxiaobei")
    yanzhengma = (By.ID, "TANGRAM__PSP_10__error")
    user_error_hint_loc = (By.ID, "TANGRAM__PSP_10__error")
    pawd_error_hint_loc = (By.ID, "TANGRAM__PSP_10__error")
    user_login_success_loc = (By.LINK_TEXT, u'john200e')

    def click_link(self):
        self.find_element(*self.link_loc).click()
        time.sleep(3)  # 等待3秒，等待登录弹窗加载完成

    def click_username(self):
        self.find_element(*self.username_loc).click()
        time.sleep(3)

    def run_case(self, value1, value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.password_loc).send_keys(value2)
        time.sleep(10)
        self.find_element(*self.submit_loc).click()
        time.sleep(5)

    def get_username(self):
        return self.find_element(*self.username_top).text

    def get_yanzhengma(self):
        return self.find_element(*self.yanzhengma).text

        # 用户名错误提示

    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

        # 密码错误提示

    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

        # 登录成功用户名

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
