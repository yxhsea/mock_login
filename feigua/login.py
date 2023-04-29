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

    # 打开飞瓜首页
    page.goto("https://dy.feigua.cn//")

    # 点击 右上角登录按钮
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//div[@class=\"header-btn \"]")

    # 点击 手机登录 Tab 栏
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//a[@data-logintype=\"phonepwd\"]")

    # 填写 账号、密码
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.fill("xpath=//input[@id=\"fb_login_phonepwd_tel\"]", "xxxxxxxxx")
    page.fill("xpath=//input[@id=\"fb_login_phonepwd_pwd\"]", "xxxxxxxxx")

    # 点击 同意用户协议
    page.evaluate("document.getElementById(\"cbAgree2\").checked = true")

    # 点击 确定
    page.wait_for_timeout(random.randint(2, 5) * 1000)
    page.click("xpath=//a[@id=\"fb_login_phonepwd_btnyes\"]")

    page.wait_for_timeout(random.randint(10, 15) * 1000)
    cookies = context.cookies()
    with open("cookies.txt", 'w') as f:
        f.write(json.dumps(cookies))

    # 关闭资源
    page.wait_for_timeout(random.randint(500, 1000) * 1000)
    page.close()
    context.close()
    browser.close()
    playwright.stop()


if __name__ == "__main__":
    pass
