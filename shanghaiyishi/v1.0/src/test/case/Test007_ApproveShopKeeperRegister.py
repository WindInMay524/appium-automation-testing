import unittest
import sys
import time
sys.path.append("..")
from page.RetailStorePage import RetailStorePage
from selenium import webdriver
from appium import webdriver
from page.BasePage import BasePage
from page.CommonPage import CommonPage
from page import WebsiteBackgroundPage
from common import CommonConfiguration as cc
from page.CustomerManagerPage import CustomerManagerPage
from page.SaleManagerPage import SaleManagerPage
from common import LogUnility as logOutput

class TestApproveShopKeeperRegister(unittest.TestCase):
    def setUp(self):
        logOutput.log.logger.info('***************Test approve shopkeeper register**************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.retail_store = RetailStorePage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)
        self.customer = CustomerManagerPage(self.appium_driver)
        self.sale_manager = SaleManagerPage(self.appium_driver)

    def testApproveRegisterApplication(self):
        self.common.changeAccount(1)
        self.editInformation()
        self.retail_store.getScreenshot()
        self.retail_store.ensureButton()
        assert ('零售店信息' in self.appium_driver.title)
        self.retail_store.getScreenshot()
        WebsiteBackgroundPage.approveReview()  # approved by backstage
        for x in range(5):
            self.appium_driver.press_keycode(4)
            time.sleep(2)
        self.retail_store.switchToNative()
        self.common.changeAccount(0)
        self.common.enterYiShiAccount()
        self.customer.getScreenshot()
        self.customer.approveShopkeeper()
        assert ('审核详细信息' in self.appium_driver.title)
        self.customer.getScreenshot()
        for x in range(4):
            self.appium_driver.press_keycode(4)
            time.sleep(2)
        self.customer.switchToNative()
        self.addCertificate()
        self.sale_manager.getScreenshot()
        self.sale_manager.confirmAddition()
        self.assertEqual('代销证详情',self.appium_driver.title)
        self.sale_manager.getScreenshot()

    def editInformation(self):
        '''
        edit information by retail shop owner
        '''

        self.common.enterYiShiAccount()
        self.retail_store.enterRetailStore()
        self.retail_store.switchToWebview()
        self.retail_store.switchToWindow(RetailStorePage.identity_front)
        self.retail_store.slipPage(RetailStorePage.tobacco_certificate)
        self.retail_store.clickFillInButton()
        self.retail_store.editOnceMore()

    def addCertificate(self):
        '''
        add certification by sale manager
        '''
        self.sale_manager.enterSaleManager()
        self.sale_manager.enterCertificate()
        self.sale_manager.editCertificate()
        self.retail_store.uploadIdPhoto(self.sale_manager.certificate_photo,1)


    def tearDown(self):
        self.appium_driver.quit()
