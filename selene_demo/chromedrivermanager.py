# -*- coding: utf-8 -*-
# @Author	: guo
# @file		: chromedrivermanager.py
# @time		: 2018/7/24 01:19

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeDriverManager:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("disable-extensions")
        self.chrome_options.add_argument('disable-logging')
        self.chrome_options.add_argument('test-type')
        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_argument('incognito')

    def set_driver_options(self, driver_options):
        self.chrome_options = driver_options

    def get_driver_instance(self):
        chrome_driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return chrome_driver

