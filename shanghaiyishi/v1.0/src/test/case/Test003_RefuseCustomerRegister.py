import unittest
import sys
import time
sys.path.append("..")
from page.CustomerManagerPage import CustomerManagerPage
from selenium import webdriver
from appium import webdriver
from page.BasePage import BasePage
from page.CommonPage import CommonPage
from page import WebsiteBackgroundPage
from common import CommonConfiguration as cc

class TestRefuseCustomerRegister(unittest.TestCase):
    def setUp(self):
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.customer_manager = CustomerManagerPage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)

    def testRefuseRegisterApplication(self):
        self.common.enterYiShiAccount()
        self.customer_manager.enterCustomerManager()
        time.sleep(4)
        self.customer_manager.editInformation()
        self.customer_manager.getScreenshot()
        self.customer_manager.ensureButton()
        assert ('客户经理信息' in self.appium_driver.title)
        time.sleep(2)
        self.appium_driver.press_keycode(4)
        time.sleep(2)
        self.appium_driver.press_keycode(4)
        self.customer_manager.getScreenshot()
        WebsiteBackgroundPage.refuseCustomer()
        time.sleep(2)
        self.customer_manager.getScreenshot()

    def tearDown(self):
        self.appium_driver.quit()