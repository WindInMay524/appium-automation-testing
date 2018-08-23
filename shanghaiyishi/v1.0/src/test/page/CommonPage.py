#-*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import time
import sys
sys.path.append("..")
from page.BasePage import BasePage
from common import LogUnility as logOutput

class CommonPage(BasePage):
    me_element = (By.XPATH,'//android.widget.TextView[@text="我"]')
    setting = (By.XPATH,'//android.widget.TextView[@text="设置"]')
    change_account = (By.XPATH,'//android.widget.TextView[@text="切换帐号"]')
    choose_account = (By.ID,'com.tencent.mm:id/d9u')
    wechat_contacts = (By.XPATH, '//android.widget.TextView[@text="通讯录"]')  # 通讯录
    wechat_account = (By.XPATH, '//android.widget.TextView[@text="公众号"]')  # 公众号
    wechat_yishi = (By.XPATH, '//android.widget.TextView[@text="意视信息科技"]')  # 意视信息科技
    detail_tag = (By.ID,'com.tencent.mm:id/hh')
    clear_content = (By.XPATH,'//android.widget.TextView[@text="清空内容"]')
    ensure_clear = (By.ID,'com.tencent.mm:id/an3')

    def changeAccount(self,account):
        '''
        change weixin account
        :param account:
        '''
        self.clickButton(self.me_element)  # 点击我的设置
        self.clickButton(self.setting)  # 点击设置
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x = int(x * 0.9)
        y = int(y * 0.9)
        self.logOutput(x)
        self.logOutput(y)
        self.driver.swipe(x, y, x, y, 5)
        '''
        self.clickButton(self.change_account)
        ele = self.findElement(self.choose_account)
        eles = ele.find_elements_by_class_name('android.widget.FrameLayout')
        eles[int('%d' % account)].click()
        time.sleep(5)
        if self.isElement(self.change_account):
            logOutput.log.logger.info('It is the current account,no need to change')
            self.driver.press_keycode(4)
            time.sleep(2)

    def enterYiShiAccount(self):
        '''
        enter yishi account
        '''
        self.findElement(self.wechat_contacts)
        logOutput.log.logger.info('Enter shanghaiyishi account')
        self.clickButton(self.wechat_contacts)  # 进入通讯录
        self.clickButton(self.wechat_account)  # 进入公众号
        self.findElement(self.wechat_yishi)
        self.clickButton(self.wechat_yishi)  # 进入上海意视公众号

    def clearInformation(self):
        self.clickButton(self.detail_tag)
        self.clickButton(self.detail_tag)
        self.clickButton(self.setting)
        self.clickButton(self.clear_content)
        self.clickButton(self.ensure)
        self.driver.presskeycode(66)




