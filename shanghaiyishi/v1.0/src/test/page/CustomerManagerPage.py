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

class CustomerManagerPage(BasePage):
    customer_button = (By.XPATH,'//android.widget.TextView[@text="服务中心"]')
    customer_tab = (By.XPATH,'//android.widget.TextView[@text="客户经理"]')
    customer_name = (By.XPATH,'//div[@class="pb-20"]/div/div[1]/div/div[2]/input')
    identification_number = (By.XPATH,'//div[@class="pb-20"]/div/div[2]/div/div[2]/input')
    business_district = (By.XPATH,'//div[@class="pb-20"]/div/div[3]/div/div[2]')
    shanghai_province = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[1]/div[9]')
    province_city = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[2]/div')
    city_dirstrict = (By.XPATH,'//div[@class="mod-address-body"]/div[2]/div/div/div[3]/div[1]')
    iphone_number = (By.XPATH,'//div[@class="pb-20"]/div/div[4]/div/div[1]/div[2]/input')
    verification_code = (By.XPATH,'//div[@class="pb-20"]/div/div[4]/div/div[2]/div[2]/input')
    next_button = (By.CSS_SELECTOR,'button.sub-btn')
    ensure_button = (By.CSS_SELECTOR,'button.swal-button.swal-button--confirm')
    shop_detail = (By.XPATH,'//android.widget.TextView[@text="详情"]')
    checking_tab = (By.LINK_TEXT,'待审核')
    enter_shop = (By.XPATH,'//div[@class="mint-tab-container-wrap"]/div[1]/div')
    refuse_button = (By.XPATH,'//div[@class="confirm-btns"]/button[1]')
    agree_button = (By.XPATH,'//div[@class="confirm-btns"]/button[2]')
    refuse_reason = (By.XPATH,'//div[@class="model-panel"]/div[1]/div[2]/div[2]/div[2]')
    refuse_ensure = (By.XPATH,'//div[@class="model-panel"]/div[2]/div[2]')
    agree_ensure = (By.CSS_SELECTOR,'button.mint-msgbox-btn.mint-msgbox-confirm')
    refused_tab = (By.LINK_TEXT,'已拒绝')
    refused_detail = (By.XPATH,'//div[@class="review-page"]/div[1]/div[1]')
    approved_tab = (By.LINK_TEXT,'已通过')
    approved_information = (By.XPATH,'//div[@class="review-page"]/div[1]/div[1]')
    refuse_information = (By.XPATH,'//ul[@class="list"]/div[5]/div[2]')

    def enterCustomerManager(self):
        '''
        enter customer manager page
        '''
        logOutput.log.logger.info('Enter customer manager page')
        self.clickButton(self.customer_button)
        self.clickButton(self.customer_tab)

    def editInformation(self):
        '''
        edit customer manager registration information
        '''
        self.switchToWebview()
        self.switchToWindow(self.customer_name)
        self.sendKeys(self.customer_name,cc.customerName())
        self.sendKeys(self.identification_number,random.randint(0,1000000000000000))
        self.clickButton(self.business_district)
        time.sleep(2)
        self.clickButton(self.shanghai_province)
        self.clickButton(self.province_city)
        self.clickButton(self.city_dirstrict)
        self.sendKeys(self.iphone_number,cc.customerIphone())
        self.sendKeys(self.verification_code,cc.verificationCode())
        self.driver.hide_keyboard()
        time.sleep(2)

    def editInformationAgain(self):
        '''
        shopkeeper edit error information again
        '''
        self.switchToWebview()
        self.switchToWindow(self.verification_code)
        self.sendKeys(self.verification_code, cc.verificationCode())

    def ensureButton(self):
        try:
            self.switchToWindow(self.next_button)
            self.clickButton(self.next_button)
            self.clickButton(self.ensure_button)
        except Exception as e:
            logOutput.log.logger.info('error: %s' % e)
            self.getScreenshot()

    def reviewShopkeeper(self):
        '''
        customer manager review shopkeeper application information
        '''
        self.clickButton(self.shop_detail)
        self.switchToWebview()
        self.switchToWindow(self.checking_tab)
        self.clickButton(self.checking_tab)
        self.clickButton(self.enter_shop)

    def refuseShopkeeper(self):
        '''
        customer manager refuse shopkeeper application
        '''
        self.reviewShopkeeper()
        self.clickButton(self.refuse_button)
        self.clickButton(self.refuse_reason)
        self.clickButton(self.refuse_ensure)
        self.switchToWindow(self.refused_tab)
        time.sleep(2)
        self.clickButton(self.refused_tab)
        self.clickButton(self.refused_detail)

    def approveShopkeeper(self):
        '''
        customer manager approve shopkeeper application
        '''
        self.reviewShopkeeper()
        self.clickButton(self.agree_button)
        self.clickButton(self.agree_ensure)
        self.switchToWindow(self.approved_tab)
        time.sleep(2)
        self.clickButton(self.approved_tab)
        self.clickButton(self.approved_information)

