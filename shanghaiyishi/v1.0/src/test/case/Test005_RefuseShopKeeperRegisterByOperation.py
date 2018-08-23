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
from common import LogUnility as logOutput

class TestRefuseShopKeeperRegisterByOperation(unittest.TestCase):

    def setUp(self):
        logOutput.log.logger.info('****************Test shop keeper refused by operation****************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(),BasePage.desired_caps)
        self.retail_store = RetailStorePage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)

    def testRefuseRegisterApplication(self):
        self.common.changeAccount(1)
        self.editInformation()
        WebsiteBackgroundPage.refuseReview()	#refused by backstage
        for x in range(3):
            self.appium_driver.press_keycode(4)
            time.sleep(2)
        time.sleep(5)
        self.retail_store.getScreenshot()

    def editInformation(self):
        '''
        edit information by retail shop owner
        '''
        self.common.enterYiShiAccount()
        self.retail_store.enterRetailStore()
        self.retail_store.switchToWebview()
        self.retail_store.switchToWindow(RetailStorePage.identity_front)
        self.retail_store.uploadIdPhoto(RetailStorePage.identity_front, 3)
        self.retail_store.slipPage(RetailStorePage.tobacco_certificate)
        self.retail_store.uploadIdPhoto(RetailStorePage.identity_reverse, 2)
        self.retail_store.uploadIdPhoto(RetailStorePage.tobacco_certificate, 1)
        self.retail_store.uploadIdPhoto(RetailStorePage.business_license, 0)
        self.retail_store.clickFillInButton()
        self.retail_store.chooseDistrict()
        self.retail_store.chooseCustomerManager()
        self.retail_store.editInformation()
        self.retail_store.getScreenshot()
        self.retail_store.ensureButton()
        assert ('零售店信息' in self.appium_driver.title)
        self.retail_store.getScreenshot()
        time.sleep(2)

    def tearDown(self):
        self.appium_driver.quit()

