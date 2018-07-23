# -*- coding: utf-8 -*-
# @Author	: guo
# @file		: open_url.py
# @time		: 2018/7/24 01:15

from chromedrivermanager import ChromeDriverManager
from selene import browser, config
from selene.support.jquery_style_selectors import s
from selene.api import have


def setUp(self):
    chrome_driver = ChromeDriverManager().get_driver_instance()
    browser.set_driver(chrome_driver)
    config.base_url = 'http://www.jd.com'


def tearDown(self):
    browser.close()


class TestCaseNopLoginFunc:
    # def test_login_success(self):
    #     browser.open_url('/login')
    #     s('.login-notices').should(have.value('密码登录在这里'))
    #     s('.scan-tear-angle pc').click()
    #     s('.hwid2').should(have.value('折800账号登录'))
    #
    #     s('#ddusername.t').send_keys('error_name')
    #     s('#ddpw_1_text').send_keys('123456')
    #     s('.login-button').click()

    # def test_login_failure(self):
    #     browser.open_url('/login')
    #     s('.login-button').should(have.value('Log in'))
    #
    #     s('#Email').send_keys('wjm19851120@163.com')
    #     s('#Password').send_keys('12345555555')
    #     s('.login-button').click()
    #
    #     s('.validation-summary-errors span').should(have.exact_text(
    #         'Login was unsuccessful. Please correct the errors and try again.')
    #     )

    def test_login_fail(self):
        browser.open_url('/login')
        s('.login-notices').should(have.value('密码登录在这里'))
        s('.scan-tear-angle pc').click()
        s('.hwid2').should(have.value('折800账号登录'))

        s('#ddusername.t').send_keys('error_name')
        s('#ddpw_1_text').send_keys('123456')
        s('.login-button').click()

        s('#pperrmsg.error').should(have.exact_text('请完成滑块验证'))


if __name__ == '__main__':

