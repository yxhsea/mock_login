#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
from playwright.sync_api import sync_playwright


def login():
    # 初始化 Playwright、启动 Chromium 浏览器
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=[
        '--disable-blink-features=AutomationControlled',
        '--no-sandbox'
    ])
    context = browser.new_context()
    page = context.new_page()

    # 打开抖查查首页
    page.goto("https://www.douchacha.com/")

    # 点击 登录按钮
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//p[@class=\"login_txt\"]//span[@class=\"login\"]")

    # 点击 手机登录 Tab 栏
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//a[@class=\"login_dialog_switch\"]")

    # 填写 账号、密码
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.fill("xpath=//input[@placeholder=\"请输入手机号\"]", "xxxxx")
    page.fill("xpath=//input[@placeholder=\"请输入密码\"]", "xxxxx")

    # 点击 确定
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//div[@class=\"login_warp\"]//div[@class=\"login_input_warp\"]//button//span[contains(text(), \"登录\")]")

    page.wait_for_timeout(random.randint(10, 15) * 1000)
    cookies = context.cookies()
    with open("cookies.txt", 'w') as f:
        f.write(json.dumps(cookies))

    # 关闭资源
    page.wait_for_timeout(random.randint(5, 10) * 1000)
    page.close()
    context.close()
    browser.close()
    playwright.stop()


if __name__ == "__main__":
    login()
