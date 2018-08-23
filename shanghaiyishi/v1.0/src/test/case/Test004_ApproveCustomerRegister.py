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
from common import LogUnility as logOutput

class TestApproveCustomerRegister(unittest.TestCase):
    def setUp(self):
        logOutput.log.logger.info('**************Test approve customer register****************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.customer_manager = CustomerManagerPage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)

    def testApproveRegisterApplication(self):
        self.common.changeAccount(0)
        self.common.enterYiShiAccount()
        self.customer_manager.enterCustomerManager()
        time.sleep(4)
        self.customer_manager.editInformationAgain()
        self.customer_manager.getScreenshot()
        self.customer_manager.ensureButton()
        assert ('客户经理信息' in self.appium_driver.title)
        time.sleep(2)
        WebsiteBackgroundPage.approveCustomer()
        for i in range(2):
            self.appium_driver.press_keycode(4)
            time.sleep(2)
        time.sleep(5)
        self.customer_manager.getScreenshot()

    def tearDown(self):
        self.appium_driver.quit()
