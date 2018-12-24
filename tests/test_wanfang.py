# coding:utf-8
import unittest
from selenium import webdriver
from page.wanfang_page import WanfangPage
from util import log
import time
from selenium.webdriver.support.ui import Select


class TestWanfang(unittest.TestCase):
    """UI自动化搜索"""

    def setUp(self):
        self.url = "http://fz.wanfangdata.com.cn/index.do"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.verificationErrors = []
        self.wanfang_page = WanfangPage(self.driver)
        # self.title = u'百度一下，你就知道'
        self.mylog = log.log()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_search(self):
        """搜索测试关键字"""
        try:
            sp = WanfangPage(self.driver)
            sp.open(self.url)
            sp.run_case("志")
            # sp.run_case(self.random_phone_number)
            sp.click_link()
            assert u'志' in self.driver.page_source
        except Exception as e:
            self.wanfang_page.img_screenshot(u'搜索志关键字')
            self.mylog.error(u'搜索志关键字')
            raise e

    # def test_login(self):
    #     '''登录'''
    #     try:
    #        sp = LoginPage(self.driver)
    #        sp.open(self.url)
    #        sp.click_link()
    #        sp.click_username()
    #        sp.run_case("john200e","xxxxx")
    #        self.assertEqual(sp.get_yanzhengma(),"请您输入验证码",msg="验证成功！")
    #     except Exception as e:
    #         self.search_page.img_screenshot(u'登录')
    #         self.mylog.error(u'test_search中的登录方法')
    #         raise e

    def test_select(self):
        """选择志书条目下拉框"""
        try:
            sp = WanfangPage(self.driver)
            sp.open(self.url)
            time.sleep(5)
            # select = Select(self.driver.find_element_by_id('selectedType'))
            # all_options = select.options
            # select.select_by_index(0)
            # select.select_by_visible_text("志书")
            # select.select_by_value("0")
            #
            # actual_optionsList = map(lambda option:option.text,all_options)
            # for i in actual_optionsList:
            #     print (i)

            # 去勾选select.deselect_by_index(num)
            # select.deselect_by_index(2)
            s = self.driver.find_element_by_id("selectedType")
            Select(s).select_by_value("1")
            # print(Select(s).select_by_value("1"))
            # self.driver.find_element_by_id("selectedType").click()
            # self.assertEqual(Select(s).select_by_value("1"), u'条目', msg=u'验证成功！')
            assert u'xxx条目' in Select(s).all_selected_options()
        except Exception as e:
            self.wanfang_page.img_screenshot(u'复选框')
            self.mylog.error(u'复选框报错！')


    # def test_search_text_field_max_length(self):
    #     # get the search textbox
    #     search_field = self.driver.find_element_by_id('search')
    #     # check maxlength attribute is set to 128
    #     self.assertEqual('128', search_field.get_attribute('maxlength'))
    #
    # def test_search_button_enabled(self):
    #     # get Search button
    #     search_button = self.driver.find_element_by_class_name('button')
    #     # check Search button is enabled
    #     self.assertTrue(search_button.is_enabled())
    #
    # def test_my_account_link_is_displayed(self):
    #     # get the Account link
    #     account_link = self.driver.find_element_by_link_text('ACCOUNT')
    #     # check My Account link is displayed/visible in the Home page footer
    #     self.assertTrue(account_link.is_displayed())
    #
    # def test_account_links(self):
    #     # get the all the links with Account text in it
    #     account_links = self.driver.find_elements_by_partial_link_text('ACCOUNT')
    #     # check Account and My Account link is displayed/visible in the Home page footer
    #     self.assertTrue(len(account_links), 2)
    #
    # def test_count_of_promo_banners_images(self):
    #     # get promo banner list
    #     banner_list = self.driver.find_element_by_class_name('promos')
    #     # get images from the banner_list
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     # check there are 3 banners displayed on the page
    #     self.assertEqual(3, len(banners))
    #
    # def test_vip_promo(self):
    #     # get vip promo image
    #     vip_promo = self.driver.find_element_by_xpath("//img[@alt='Shop Private Sales - Members Only']")
    #     # check vip promo logo is displayed on home page
    #     self.assertTrue(vip_promo.is_displayed())
    #     # click on vip promo images to open the page
    #     vip_promo.click()
    #     # check page title
    #     self.assertEqual("VIP", self.driver.title)
    #
    # def test_shopping_cart_status(self):
    #     # check content of My Shopping Cart block on Home page
    #     # get the Shopping cart icon and click to open the Shopping Cart section
    #     shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')
    #     shopping_cart_icon.click()
    #     # get the shopping cart status
    #     shopping_cart_status = self.driver.find_element_by_css_selector('p.empty').text
    #     self.assertEqual('You have no items in your shopping cart.', shopping_cart_status)
    #     # close the shopping cart section
    #     close_button = self.driver.find_element_by_css_selector('div.minicart-wrapper a.close')
    #     close_button.click()
