# coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from util import log
from selenium.webdriver.common.by import By
from config.globalparameter import img_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

'''
这个类主要是完成所有页面的一些公共方法的封装

'''


class Action(object):
    # 初始化
    def __init__(self, se_driver):
        self.driver = se_driver
        # self.title = page_title
        self.mylog = log.log()

        self.wait = WebDriverWait(self.driver, 30)
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }

    # 封装高亮显示页面元素的方法
    # 使用javascript代码将传入的页面元素对象的背景颜色和边框颜色分别设置为绿色和红色
    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background:green; border:2px solid red;")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        self.mylog.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        self.mylog.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        self.mylog.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            self.mylog.info("Closing and quit the browser.")
        except NameError as e:
            self.mylog.error("Failed to quit the browser with %s" % e)

    #  打开页面，并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, u'打开页面失败：s%' % url
        except:
            self.mylog.error(u"未能正确打开页面：" + url)

    # 截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path + img_name + '.png')
        except:
            self.mylog.error(u'截图失败:' + img_name)

    # 定义open方法
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 重写元素定位的方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s",  *loc)

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.excute_script(src)

    # 重写send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % (self, loc))

    def frame_avaliable_and_switch_to_it(self, locationType, locatorExpression):
        '''检查frame 是否存在，存在则切换进frame控件中'''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            raise self.mylog.error(u'没有frame' + locationType + locatorExpression)

    def visibility_element_located(self, locationType, locatorExpression):
        '''显式等待页面元素的出现'''
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            print(element)

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义open方法，调用_open()进行打开链接
    # def open(self):
    #     self._open(self.base_url, self.pagetitle)

    # 使用current_url获取当前窗口url地址，进行与配置地址作比较，返回比较结果(True False)
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.excute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # # 定位元素方法
    # def find_element(self, selector):
    #     """
    #      这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
    #      submit_btn = "id=>su"
    #      login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
    #      如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
    #     :param selector:
    #     :return: element
    #     """
    #     element = ''
    #     if '=>' not in selector:
    #         return self.driver.find_element_by_id(selector)
    #     selector_by = selector.split('=>')[0]
    #     selector_value = selector.split('=>')[1]
    #
    #     if selector_by == "i" or selector_by == 'id':
    #         try:
    #             element = self.driver.find_element_by_id(selector_value)
    #             self.mylog.info("Had find the element \' %s \' successful "
    #                         "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             self.mylog.error("NoSuchElementException: %s" % e)
    #             # take screenshot
    #             self.img_screenshot(u'base_page:find_element:error' + "NoSuchElementException: %s" % e)
    #     elif selector_by == "n" or selector_by == 'name':
    #         element = self.driver.find_element_by_name(selector_value)
    #     elif selector_by == "c" or selector_by == 'class_name':
    #         element = self.driver.find_element_by_class_name(selector_value)
    #     elif selector_by == "l" or selector_by == 'link_text':
    #         element = self.driver.find_element_by_link_text(selector_value)
    #     elif selector_by == "p" or selector_by == 'partial_link_text':
    #         element = self.driver.find_element_by_partial_link_text(selector_value)
    #     elif selector_by == "t" or selector_by == 'tag_name':
    #         element = self.driver.find_element_by_tag_name(selector_value)
    #     elif selector_by == "x" or selector_by == 'xpath':
    #         try:
    #             element = self.driver.find_element_by_xpath(selector_value)
    #             self.mylog.info("Had find the element \' %s \' successful "
    #                         "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             self.mylog.error("NoSuchElementException: %s" % e)
    #             # take screenshot
    #             self.img_screenshot(u'base_page:find_element:error' + "NoSuchElementException: %s" % e)
    #     elif selector_by == "s" or selector_by == 'selector_selector':
    #         element = self.driver.find_element_by_css_selector(selector_value)
    #     else:
    #         raise NameError("Please enter a valid type of targeting elements.")
    #
    #     return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            self.mylog.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            self.mylog.error("Failed to type in input box with %s" % e)
            self.img_screenshot("Failed to type in input box with %s" % e)

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            self.mylog.info("Clear text in input box before typing.")
        except NameError as e:
            self.mylog.error("Failed to clear in input box with %s" % e)
            self.img_screenshot("Failed to clear in input box with %s" % e)

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            self.mylog.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            self.mylog.error("Failed to click the element with %s" % e)

    # 网页标题
    def get_page_title(self):
        self.mylog.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 判断元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 登录轻享硬件分时租赁管理平台
    def login(self, username, passwd):
        """usage: login(username="xxx", passwd="yyy" )"""
        url = "http://hardware.qingxiangchuxing.com/login"
        xpath = "/html/frameset/frame[1]"
        input_loc = (By.NAME, "loginName")
        name_loc = (By.NAME, "password")
        submit_loc = (By.ID, "loginBtn")
        self.open(url)
        frame1 = self.driver.find_element_by_xpath(xpath)
        self.switch_frame(frame1)
        self.find_element(*input_loc).send_keys(username)
        self.find_element(*name_loc).send_keys(passwd)
        time.sleep(3)
        self.find_element(*submit_loc).click()

