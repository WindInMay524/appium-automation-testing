#-*- coding: utf-8 -*-
from selenium import webdriver
import sys
import random
import time
from selenium.webdriver.common.by import By
sys.path.append("..")
from common import CommonConfiguration as cc
from common import LogUnility as logOutput
from page.BasePage import BasePage


class WebsiteBackgroundPage(BasePage):
#    global selenium_driver
    username = (By.ID,'email')
    password = (By.ID,'password')
    login_button = (By.XPATH,'//form[@id="loginForm"]/button')
    identification_tab = (By.LINK_TEXT,'认证')
    store_tab = (By.LINK_TEXT,'零售店')
    detail_iframe = 'contentFrame'
    edit_tab = (By.XPATH,'//td[@class="operation"]/a[1]/i')
    storekeeper_name = (By.NAME,'name')
    detail_address = (By.ID,'address')
    store_name = (By.NAME,'view_name')
    identification_card = (By.NAME,'id_number')
    tobacco_card = (By.NAME,'yan_code')
    choose_lottery = (By.XPATH,'//select[@name="ticket_type"]')
    sports_lottery = (By.XPATH,'//select[@name="ticket_type"]/option[2]')
    submit_button = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    check_state = (By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[11]')
    choose_reason = (By.XPATH,'//select[@id="reason"]')
    identification_reason = (By.XPATH,'//select[@id="reason"]/option[4]')
    customer_tab = (By.LINK_TEXT,'客户经理')
    refuse_tab = (By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[12]/span/a[2]')
    approve_tab = (By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[12]/span/a[1]')
    ensure_approve = (By.XPATH,'//div[@class="dialogBottom"]/input[1]')
    sale_tab = (By.LINK_TEXT,'访销')
    salesman_manage = (By.LINK_TEXT,'访销经理管理')
    approve_salesman = (By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[7]/span/a[1]/i')
    refuse_salesman = (By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[7]/span/a[2]/i')
    ensure_salesman = (By.ID,'pass')

    def loginWebdriver(self):
        '''
        login website and judge whether the page logged in
        '''
        self.driver.get(cc.baseUrl())
        element = self.isElement(self.identification_tab)
        if not element:
            logOutput.log.logger.info('Need to login firstly')
            time.sleep(3)
            self.sendKeys(self.username,cc.username())
            self.sendKeys(self.password,cc.password())
            self.clickButton(self.login_button)
        else:
            self.logOutput("Don't need to login")

    def enterStore(self):
        '''
        operational people enter store page and check registration Information
        '''
        self.clickButton(self.identification_tab)
        self.clickButton(self.store_tab)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.switch_to.frame(self.detail_iframe)
        self.clickButton(self.edit_tab)

    def enterCustomerManager(self):
        '''
        operational people enter customer page and check registration Information
        '''
        self.clickButton(self.identification_tab)
        self.clickButton(self.customer_tab)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.switch_to.frame(self.detail_iframe)

    def enterSaleManager(self):
        '''
        operational people enter salesman page and check registration Information
        '''
        self.clickButton(self.sale_tab)
        self.clickButton(self.salesman_manage)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.switch_to.frame(self.detail_iframe)

    def approveShopkeeperApplication(self):
        '''
        operational people approve shopkeeper application
        '''
        self.sendKeys(self.storekeeper_name,cc.storekeeperName())
        self.sendKeys(self.detail_address,cc.detailAddress())
        self.sendKeys(self.store_name,cc.storeName())
        self.sendKeys(self.identification_card,random.randint(0,1000000000000000))
        self.sendKeys(self.tobacco_card,random.randint(0,1000000))
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(self.findElement(self.choose_lottery)).perform()
        self.clickButton(self.sports_lottery)
        time.sleep(2)
        self.scrollToDown()
        time.sleep(2)
        self.clickButton(self.submit_button)
 #       self.driver.refresh()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.switch_to.frame(self.detail_iframe)
        time.sleep(3)
        ele = self.findElement(self.check_state)
        if ele.text == "资料审核已通过":
            logOutput.log.logger.info('Get approved by website backstage')
        else:
            self.exception('Failly approved by website backstage ')

    def refuseShopkeeperApplication(self):
        '''
        operational people refuse shopkeeper application
        '''
        self.scrollToDown()
        time.sleep(2)
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(self.findElement(self.choose_reason)).perform()
        self.clickButton(self.identification_reason)
        self.clickButton(self.submit_button)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.switch_to.frame(self.detail_iframe)
        time.sleep(2)
        ele = self.findElement(self.check_state)
        if ele.text == "已拒绝":
            logOutput.log.logger.info('Refused by website backstage in some reason ')
        else:
            self.exception('Failly Resused by website backstage ')

    def approveCustomerApplication(self):
        self.clickButton(self.approve_tab)
        time.sleep(2)
        self.clickButton(self.ensure_approve)
        ele = self.isElement(self.ensure_approve)
        if not ele:
            logOutput.log.logger.info('Customer application approved by website backstage')
        else:
            self.exception('Customer application unsuccessfully approved by website backstage')

    def refuseCustomerApplication(self):
        self.clickButton(self.refuse_tab)
        time.sleep(2)
        self.clickButton(self.submit_button)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        ele = self.isElement(self.refuse_tab)
        if not ele:
            logOutput.log.logger.info('Customer application Refused by website backstage in some reason ')
        else:
            self.exception('Customer application Abortively Resused by website backstage ')

    def approveSalemanApplication(self):
        self.clickButton(self.approve_salesman)
        time.sleep(3)
        self.clickButton(self.ensure_salesman)
        time.sleep(2)
        ele = self.isElement(self.approve_salesman)
        if not ele:
            logOutput.log.logger.info('Salesman application approved by website backstage in some reason ')
        else:
            self.exception('Salesman application failed checked by website backstage ')

    def refuseSalesmanApplication(self):
        self.clickButton(self.refuse_salesman)
        time.sleep(2)
        self.clickButton(self.submit_button)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        ele = self.isElement(self.refuse_salesman)
        if not ele:
            logOutput.log.logger.info('Salesman application Refused by website backstage in some reason ')
        else:
            self.exception('Salesman application Abortively Resused by website backstage ')

    def quitChrome(self):

        self.driver.quit()

def approveReview():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterStore()
    backstage_page.approveShopkeeperApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

def refuseReview():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterStore()
    backstage_page.refuseShopkeeperApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

def approveCustomer():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterCustomerManager()
    backstage_page.approveCustomerApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

def refuseCustomer():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterCustomerManager()
    backstage_page.refuseCustomerApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

def refuseSalesman():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterSaleManager()
    backstage_page.refuseSalesmanApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

def approveSalesman():
    selenium_driver = webdriver.Chrome(cc.driverPath())
    backstage_page = WebsiteBackgroundPage(selenium_driver)
    backstage_page.loginWebdriver()
    backstage_page.enterSaleManager()
    backstage_page.approveSalemanApplication()
    selenium_driver.get_screenshot_as_file(cc.picturePath())
    backstage_page.quitChrome()

#approveReview()
#refuseReview()
#refuseCustomer()




