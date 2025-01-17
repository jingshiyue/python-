# -*- coding:utf-8 -*- 
from selenium import webdriver
import sys
from .Log import MyLog as Log
sys.path.append("..")
import readConfig
import threading

localReadConfig = readConfig.ReadConfig()


class Driver:

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

        self.browser = webdriver.Chrome()

    def open_browser(self, name1, name2):
        """
        Do something for browser
        :return: browser
        """
        self.logger.info("Open browser")

        # 绐楀彛鏈�ぇ鍖�
        self.browser.maximize_window()

        # 鎵撳紑鍦板潃閾炬帴
        url = localReadConfig.get_webServer(name1, name2)
        self.logger.info("url:%s" %url)
        self.browser.get(url)
        return self.browser

    def close_browser(self):
        """
        quit browser
        :return:
        """
        self.browser.quit()
        self.logger.info("Quit browser")

    def get_driver(self):
        """
        get web driver
        :return:
        """
        return self.browser


class MyDriver:

    driver = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_browser():

        if MyDriver.driver is None:
            MyDriver.mutex.acquire()
            MyDriver.driver = Driver()
            MyDriver.mutex.release()

        return MyDriver.driver

#if __name__ == "__main__":
    #driver = MyDriver.get_browser()
    #browser = driver.open_browser("SHEIN","www")
