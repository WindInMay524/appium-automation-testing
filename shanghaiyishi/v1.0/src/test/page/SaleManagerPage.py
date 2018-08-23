#-*- coding: utf-8 -*-
__author__ = 'TinaTang'
import sys
import random
import time
from selenium.webdriver.common.by import By
sys.path.append("..")
from common import CommonConfiguration as cc
from common import LogUnility as logOutput
from page.BasePage import BasePage

class SaleManagerPage(BasePage):
    customer_button = (By.XPATH,'//android.widget.TextView[@text="服务中心"]')
    saler_tab = (By.XPATH,'//android.widget.TextView[@text="访销经理"]')
    saler_name = (By.XPATH,'//div[@id="app"]/div/div[1]/div/div/div[2]/input')
    identification_number = (By.XPATH,'//div[@id="app"]/div/div[2]/div/div/div[2]/input')
    business_district = (By.XPATH,'//div[@id="app"]/div/div[3]/div/div/div[2]')
    shanghai_province = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[1]/div[9]')
    province_city = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[2]/div')
    city_dirstrict = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[3]/div[1]')
    belong_company = (By.XPATH,'//div[@id="app"]/div/div[4]/div/div/div[2]/input')
    iphone_number = (By.XPATH,'//div[@id="app"]/div/div[5]/div/div/div[1]/div[2]/input')
    verification_code = (By.XPATH,'//div[@id="app"]/div/div[5]/div/div/div[2]/div[2]/input')
    submit_button = (By.CSS_SELECTOR,'button.sub-btn')
    determine_button = (By.CSS_SELECTOR,'button.swal-button.swal-button--confirm')
    certificate_manage = (By.XPATH,'//div[@id="app"]/div/div[2]')
    add_certificate = (By.XPATH,'//div[@class="i-position"]/i')
    shop_name = (By.XPATH,'//div[@class="list-group"]/div[1]/div[2]/input')
    shopkeeper_iphone = (By.XPATH,'//div[@class="list-group"]/div[2]/div[2]/input')
    certificate_number = (By.XPATH,'//div[@class="list-group"]/div[3]/div[2]/input')
    certificate_photo = (By.XPATH,'//div[@class="list-group"]/div[4]/div[2]/div')
    ensure_button = (By.CSS_SELECTOR,'button.btn.custom-btn.btn-block.w-80')
    confirm_button = (By.CSS_SELECTOR,'button.mint-msgbox-btn.mint-msgbox-confirm')
    certificate_detail = (By.XPATH,'//div[@id="app"]/div/ul/li')

    def enterSaleManager(self):
        logOutput.log.logger.info('Enter sale manager page')
        time.sleep(2)
        self.clickButton(self.customer_button)
        self.clickButton(self.saler_tab)

    def editInformation(self):
        self.switchToWindow(self.saler_name)
        self.sendKeys(self.saler_name,cc.salerName())
        time.sleep(2)
        self.sendKeys(self.identification_number,random.randint(0,1000000000000000))
        self.clickButton(self.business_district)
        self.clickButton(self.shanghai_province)
        self.clickButton(self.province_city)
        self.clickButton(self.city_dirstrict)
        self.sendKeys(self.belong_company,cc.belongCompany())
        self.sendKeys(self.iphone_number,cc.salerIphone())
        self.sendKeys(self.verification_code,cc.verificationCode())
        self.driver.hide_keyboard()

    def editInformationAnew(self):
        self.switchToWindow(self.verification_code)
        self.sendKeys(self.verification_code, cc.verificationCode())
 #       self.driver.hide_keyboard()

    def ensureButton(self):
        try:
            self.switchToWindow(self.submit_button)
            self.clickButton(self.submit_button)
            self.clickButton(self.determine_button)
        except Exception as e:
            logOutput.log.logger.info('error: %s' % e)
            self.getScreenshot()


    def enterCertificate(self):
        self.switchToWebview()
        self.switchToWindow(self.certificate_manage)
        self.clickButton(self.certificate_manage)

    def editCertificate(self):
        self.clickButton(self.add_certificate)
        self.sendKeys(self.shop_name,cc.storekeeperName())
        self.sendKeys(self.shopkeeper_iphone,cc.shopkeeperIphone())
        self.sendKeys(self.certificate_number,random.randint(0,1000000))

    def confirmAddition(self):
        self.clickButton(self.ensure_button)
        self.clickButton(self.confirm_button)
        self.clickButton(self.certificate_detail)
