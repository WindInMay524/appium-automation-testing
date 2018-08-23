#-*- coding: utf-8 -*-
__author__ = 'TinaTang'
import sys
import time
import os
import logging
sys.path.append("..")
from common import CommonConfiguration as cc
from common import LogUnility as logOutput
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """description of class"""
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    desired_caps['deviceName'] = '4b62e63e'
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
    desired_caps['automationName'] = 'UIAutomator2'
    desired_caps['recreateChromeDriverSessions'] = 'true'
    desired_caps['noReset'] = 'true'

    #webdriver instance
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,element):
        '''
        Find element
        element is a set with format (identifier type,value),e.g.('id','username')

        Usage:
        self.findElement(element)
        '''
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*element).is_displayed())
            return self.driver.find_element(*element)

        except Exception:
            raise ValueError("No such element found" + str(element))

    def findElements(self,element):
        '''
        Find elements
        element is a set with format (idertifier type,value),e.g.('id','username')

        Usage:
        self.findElements(element)
        '''
        try:
            if len(self.driver.find_elements(*element)):
                return self.driver.find_elements(*element)
        except Exception as e:
            raise ValueError("No such elements found: %s" % e)

    def sendKeys(self,element,text):
        '''
        Operation input box.

        Usage:
        self.type(element,text)
        '''
        self.findElement(element).send_keys(text)

    def clickButton(self,element):
        '''
        Click page element,like button,image,link,etc.
        '''
        self.findElement(element).click()

    def isElement(self,element):
        '''
        Determine whether a page element exists
        '''
        try:
            self.findElement(element)
            return True
        except:
            return False

    def logOutput(self):
        '''
        print log information
        '''
        return logging.basicConfig(format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                            level=logging.INFO
                            )

#		print(cc.getCurrentTime() + " " + str(info))

    def exception(self,info):
        '''
        raise an exception
        '''
        raise Exception(info)

    def switchToWebview(self):
        '''
        switch page from nativeAPP to webview
        '''
        context = cc.webviewContext()
        contexts = self.driver.contexts
        if context in contexts:
            logOutput.log.logger.info('Locate to webview succefully')
            self.driver.switch_to.context(context)
            logOutput.log.logger.info(self.driver.current_context)
        else:
            self.exception('Page cannot jump rightly')
        time.sleep(2)

    def switchToNative(self):
        '''
        switch page from webview to native
        '''
        context = self.driver.current_context
        logOutput.log.logger.info(context)
        if context == cc.webviewContext():
            self.driver.switch_to.context(cc.nativeContext())
            logOutput.log.logger.info(self.driver.current_context)
        else:
            self.exception('Page locate wrongly')
        time.sleep(2)

    def switchToWindow(self,element):
        '''
        switch page handle
        '''
        all_handles = self.driver.window_handles
        logOutput.log.logger.info(all_handles)
        for handle in all_handles:
            logOutput.log.logger.info(handle)
            try:
                self.driver.switch_to.window(handle)
                self.findElement(element)
                logOutput.log.logger.info('Element locate rightly')
                return self.findElement(element)
                break
            except Exception as e:
                logOutput.log.logger.info(e)
        time.sleep(2)

    def slipPage(self,element):
        '''
        slip page to a appointed element
        '''
        logOutput.log.logger.info('Start to slip page to a appointed element')
        appointed_element = self.switchToWindow(element)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', appointed_element)
        time.sleep(2)

    def scrollToDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def scrollToUp(self):
        self.driver.execute_script('window.scrollTo(0,0)')

    def getScreenshot(self):
        context = self.driver.current_context
        if context == "WEBVIEW_com.tencent.mm:tools":
            self.driver.switch_to.context("NATIVE_APP")
            self.driver.get_screenshot_as_file(cc.picturePath())
            time.sleep(2)
            self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        else:
            self.driver.get_screenshot_as_file(cc.picturePath())
