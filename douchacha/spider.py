#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
from playwright.sync_api import sync_playwright


def response_callback(response):
    # 过滤出商品列表接口数据
    if '/api/tiktok/search/goods' in response.url and response.status == 200:
        print(response.json())


def search_good():
    # 初始化 Playwright、启动 Chromium 浏览器
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=[
        '--disable-blink-features=AutomationControlled',
        '--no-sandbox'
    ])
    context = browser.new_context()
    # 设置 cookie
    with open("./cookies.txt", "r") as f:
        cookies = json.loads(f.read())
        context.add_cookies(cookies)
    page = context.new_page()

    # 打开抖查查商品搜索页面
    page.goto("https://www.douchacha.com/searchshopdetail")

    # 设置回调函数
    page.on('response', response_callback)

    # 关闭资源
    page.wait_for_timeout(random.randint(5, 10) * 1000)
    page.close()
    context.close()
    browser.close()
    playwright.stop()


if __name__ == "__main__":
    pass
