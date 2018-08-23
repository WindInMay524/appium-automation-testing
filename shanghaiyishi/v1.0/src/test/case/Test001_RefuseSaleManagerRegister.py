import unittest
import sys
import time
from appium import webdriver
sys.path.append("..")
from page.SaleManagerPage import SaleManagerPage
from page.BasePage import BasePage
from page.CommonPage import CommonPage
from page import WebsiteBackgroundPage
from common import CommonConfiguration as cc
from common import LogUnility as logOutput

class TestRefuseSaleManagerRegister(unittest.TestCase):
    def setUp(self):
        logOutput.log.logger.info('**************Test refuse sale manager register***************')
        self.appium_driver = webdriver.Remote(cc.remoteUrl(), BasePage.desired_caps)
        self.sale_manager = SaleManagerPage(self.appium_driver)
        self.common = CommonPage(self.appium_driver)


    def testRefuseRegisterApplication(self):
        self.common.changeAccount(0)
        self.common.enterYiShiAccount()
        self.sale_manager.enterSaleManager()
        time.sleep(4)
        self.sale_manager.switchToWebview()
        self.sale_manager.editInformation()
        self.sale_manager.getScreenshot()
        self.sale_manager.ensureButton()
        assert ('信息' in self.appium_driver.title)
        self.sale_manager.getScreenshot()
        WebsiteBackgroundPage.refuseSalesman()

    def tearDown(self):
        self.appium_driver.quit()

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRefuseSaleManagerRegister)

    unittest.TextTestRunner(verbosity=2).run(suite)

