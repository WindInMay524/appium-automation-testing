# -*- coding: utf-8 -*-
__author__ = 'TinaTang'
import sys
import time
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

sys.path.append("..")
from common import CommonConfiguration as cc
from common import LogUnility as logOutput
from page.BasePage import BasePage

'''
零售店注册页面涉及的所有页面元素-操作方法->封装
'''


class RetailStorePage(BasePage):
    retail_store = (By.XPATH, '//android.widget.TextView[@text="零售店"]')
    retail_shopkeeper = (By.XPATH, '//android.widget.TextView[@text="零售店主"]')
    identity_front = (By.XPATH, '//div[@class="load-img-box"]/div[1]/div')  # Upload identity front photo
    identity_reverse = (By.XPATH, '//div[@class="load-img-box"]/div[2]/div')  # Upload identity reverse photo
    tobacco_certificate = (By.XPATH, '//div[@class="load-img-box"]/div[3]/div')  # Upload tobacco certificate photo
    business_license = (By.XPATH, '//div[@class="load-img-box"]/div[4]/div')  # Upload business license photo
    understand_tab = (By.CSS_SELECTOR, 'button.btn-known')
    photo_album = (By.XPATH, '//android.widget.TextView[@text="相册"]')
    folder = (By.ID, 'android.miui:id/resolver_grid')
    detail_tab = (By.XPATH, '//android.widget.ImageButton[@content-desc="显示根目录"]')
    photo_zhongwei = (By.XPATH, '//android.widget.TextView[@text="beijingzhongwei"]')
    photo = (By.CLASS_NAME, 'android.widget.GridView')
    photo_ensure = (By.XPATH, '//div[@class="button-group"]/span[4]')
    #	photos = (By.CLASS_NAME,'android.widget.LinearLayout')
    fill_in = (By.XPATH, '//*[@class="sub-btn"]')
    district = (By.XPATH, '//div[@id="app"]/div/div/div/div[1]/div')
    #	area_beijing = (By.XPATH,'//div[@class = "content"]/div[2]/div/div[1]/div[1]/ul/li[1]')
    shanghai_province = (By.XPATH, '//div[@class="mod-address-body"]/div[2]/div/div/div[1]/div[9]')
    province_city = (By.XPATH, '//div[@class="mod-address-body"]/div[2]/div/div/div[2]/div')
    city_dirstrict = (By.XPATH, '//div[@class="mod-address-body"]/div[2]/div/div/div[3]/div[1]')
    district_street = (By.XPATH, '//div[@class="mod-address-body"]/div[2]/div/div/div[4]/div[1]')
    manager = (By.XPATH, '//div[@id="app"]/div/div/div/div[2]/div')
    first_manager = (By.XPATH,'//div[contains(@class,"mobileSelect") and contains(@class,"mobileSelect-show")]/div[2]/div[2]/div/div[1]/div/ul/li[1]')
    manager_ensure = (By.XPATH,'//div[contains(@class,"mobileSelect") and contains(@class,"mobileSelect-show")]/div[2]/div[1]/div/div[3]')
    ensure_button = (By.XPATH, '//div[@class="content"]/div[1]/div/div[3]')
    input_iphone = (By.XPATH, '//div[@id="app"]/div/div/div/div[3]/div/div[1]/div[2]/input')
    input_verification = (By.XPATH, '//div[@id="app"]/div/div/div/div[3]/div/div[2]/div[2]/input')
    lottery_type = (By.XPATH, '//div[@id="app"]/div/div/div/div[4]/div/div/div[2]/div/div[1]')
    signature = (By.XPATH, '//div[@id="app"]/div/div/div/div[5]/div/div[2]')
    canvas = (By.XPATH, '//div[@class="v-mask"]/div[2]/canvas')
    canvas_button = (By.CSS_SELECTOR, "span.sub-btn.mt-20")
    consignment_protocol = (By.XPATH, '//div[@id="app"]/div/div/div/div[6]/div/div/div[1]')
    close_button = (By.XPATH, '//div[@class="swal-button-container"]/button')

    def enterRetailStore(self):
        logOutput.log.logger.info('Enter ratail shoper page')
        self.clickButton(self.retail_store)
        time.sleep(2)
        self.clickButton(self.retail_shopkeeper)
        self.driver.implicitly_wait(12)

    def clickFillInButton(self):
        '''
        click fill in button
        '''
        #		self.switchToWindow(self.fill_in)
        self.clickButton(self.fill_in)
        time.sleep(2)

    def chooseDistrict(self):
        '''
        Choose district as shanghai
        '''
        logOutput.log.logger.info('Choose district as shanghai')
        self.clickButton(self.district)
        time.sleep(2)
        '''
        province = self.findElement(self.area_beijing)
        self.logOutput(province.text)
        action = webdriver.TouchActions(self.driver)
        action.scroll_from_element(province,0,320)		#choose shanghai district
        action.perform()
        time.sleep(2)
        self.clickButton(self.ensure_button)			#click ensure button
        '''
        self.clickButton(self.shanghai_province)
        self.clickButton(self.province_city)
        self.clickButton(self.city_dirstrict)
        self.clickButton(self.district_street)
        time.sleep(2)

    def chooseCustomerManager(self):
        '''
        choose customer manager
        '''
        self.clickButton(self.manager)
        time.sleep(3)
        #		self.clickButton(self.ensure_button)			#click ensure button
        action = webdriver.TouchActions(self.driver)
        manager = self.findElement(self.first_manager)
        logOutput.log.logger.info(manager.text)
        action.scroll_from_element(manager, 0, 400)
        action.perform()
        time.sleep(2)
        self.clickButton(self.manager_ensure)
        time.sleep(2)

    def uploadIdPhoto(self, button, num):
        '''
        uoload identification photo as identity_front,identity_reverse,tobacco_certificate,business_license
        '''
        self.clickButton(button)
        ele = self.isElement(self.understand_tab)
        if ele:
            self.clickButton(self.understand_tab)
            self.clickButton(button)
        else:
            logOutput.log.logger.info('Start to upload identification photos')
        self.switchToNative()
        time.sleep(2)
        logOutput.log.logger.info('Open photo album')
        album = self.isElement(self.photo_album)
        file = self.isElement(self.folder)
        if album:
            self.clickButton(self.photo_album)
            self.choosePicture(num)
        elif file:
            ele = self.findElement(self.folder)
            eles = ele.find_elements_by_class_name('android.widget.LinearLayout')
            eles[1].click()
            self.clickButton(self.detail_tab)
            self.clickButton(self.photo_album)
            self.choosePicture(num)
        else:
            self.exception('Cannot find element')

    def choosePicture(self, num):
        self.clickButton(self.photo_album)
        self.clickButton(self.photo_zhongwei)
        pic = self.findElement(self.photo)
        pics = pic.find_elements_by_class_name('android.widget.RelativeLayout')
        logOutput.log.logger.info('%d' % num)
        pics[int('%d' % num)].click()
        time.sleep(2)
        self.switchToWebview()
        if self.isElement(RetailStorePage.photo_ensure):
            logOutput.log.logger.info('Need to confirm uploading picture')
            self.clickButton(RetailStorePage.photo_ensure)
        else:
            logOutput.log.logger.info('Picture has already uploaded')

    def editInformation(self):

        '''
        input iphone number,verification,etc
        '''
        self.sendKeys(self.input_iphone, cc.shopkeeperIphone())
        self.sendKeys(self.input_verification, cc.verificationCode())
        self.clickButton(self.lottery_type)
        self.clickButton(self.signature)
        time.sleep(2)
        action = webdriver.ActionChains(self.driver)
        action.click_and_hold(self.findElement(self.canvas)).move_by_offset(10, 40). \
            move_by_offset(40, 10). \
            move_by_offset(-10, -40). \
            move_by_offset(-40, -10).perform()
        time.sleep(2)
        self.clickButton(self.canvas_button)
        self.clickButton(self.consignment_protocol)

    def ensureButton(self):
        try:
            self.clickButton(self.fill_in)
            self.clickButton(self.close_button)
        except Exception as e:
            logOutput.log.logger.info('error: %s' % e)
            self.getScreenshot()

    def editOnceMore(self):
        '''
        edit information when refused by backstage or customer manager
        '''
        self.sendKeys(self.input_verification, cc.verificationCode())
        self.clickButton(self.lottery_type)
        self.clickButton(self.consignment_protocol)

