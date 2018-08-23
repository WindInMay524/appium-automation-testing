import unittest
import sys
import time
sys.path.append("..")
from page.SaleManagerPage import SaleManagerPage
from selenium import webdriver
from appium import webdriver
from page.BasePage import BasePage
from page.CommonPage import CommonPage
from page import WebsiteBackgroundPage
from common import CommonConfiguration as cc
from common import LogUnility as logOutput
class TestApproveSaleManagerRegister(unittest.TestCase):
    def setUp(self):
        logOutput.log.logger.info('**************Test approve sale manager register*****************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.sale_manager = SaleManagerPage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)

    def testApproveRegisterApplication(self):
        self.common.changeAccount(0)
        self.common.enterYiShiAccount()
        self.sale_manager.enterSaleManager()
        time.sleep(4)
        self.sale_manager.switchToWebview()
        print(self.appium_driver.window_handles)
        self.sale_manager.editInformationAnew()
        self.sale_manager.getScreenshot()
        self.sale_manager.ensureButton()
        assert ('信息' in self.appium_driver.title)
        time.sleep(2)
        WebsiteBackgroundPage.approveSalesman()

    def tearDown(self):
        self.appium_driver.quit()

