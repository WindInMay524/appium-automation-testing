import unittest
import sys
import time
sys.path.append("..")
from page.RetailStorePage import RetailStorePage
from appium import webdriver
from page.BasePage import BasePage
from page.CommonPage import CommonPage
from page.CustomerManagerPage import CustomerManagerPage
from page import WebsiteBackgroundPage
from common import CommonConfiguration as cc
from common import LogUnility as logOutput

class TestRefuseShopKeeperRegisterByCustomer(unittest.TestCase):

    def setUp(self):
        logOutput.log.logger.info('*************Test refuse shop keeper register by customer***************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.retail_store = RetailStorePage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)
        self.customer = CustomerManagerPage(self.appium_driver)

    def testRefuseRegisterApplication(self):
        self.common.changeAccount(1)
        self.editInformationAnew()
        self.retail_store.getScreenshot()
        self.retail_store.ensureButton()
        assert ('零售店信息' in self.appium_driver.title)
        time.sleep(2)
        WebsiteBackgroundPage.approveReview()  # approved by backstage
        for x in range(5):
            self.appium_driver.press_keycode(4)
            time.sleep(2)
        self.retail_store.switchToNative()
        self.common.changeAccount(0)
        self.common.enterYiShiAccount()
        self.customer.refuseShopkeeper()
        self.assertEqual('身份信息不符',self.customer.findElement(self.customer.refuse_information).text)
        self.customer.getScreenshot()

    def editInformationAnew(self):
        self.common.enterYiShiAccount()
        self.retail_store.enterRetailStore()
        self.retail_store.switchToWebview()
        self.retail_store.switchToWindow(RetailStorePage.identity_front)
        self.retail_store.slipPage(RetailStorePage.tobacco_certificate)
        self.retail_store.clickFillInButton()
        self.retail_store.editOnceMore()

    def tearDown(self):
        self.appium_driver.quit()