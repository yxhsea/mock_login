#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
from playwright.sync_api import sync_playwright


def decryption(content):
    """
    解密算法
    :param content:
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        with open('./js/aes.js', 'r', encoding='UTF-8') as f:
            page.add_script_tag(content=f.read())
        with open('./js/mode-ecb.js', 'r', encoding='UTF-8') as f:
            page.add_script_tag(content=f.read())
        with open('./js/pako.js', 'r', encoding='UTF-8') as f:
            page.add_script_tag(content=f.read())
        with open('./js/chan.js', 'r', encoding='UTF-8') as f:
            page.add_script_tag(content=f.read())
        result = page.evaluate("decryption(\"{}\")".format(content))
        page.close()
        browser.close()

    return json.loads(result)


def get_rank_author_sales():
    cookies = {
        'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImFwcFZlcnNpb24iOiIiLCJleHBpcmVfdGltZSI6MTY4MjYyMjAwMCwiaWF0IjoxNjgyMDQ1MDIwLCJpZCI6MTc0OTM1NywicmsiOiJnMEM3SiJ9.Xf9HaIqszCmZXyT7I0GnKIESfwsw13to7qfVOZJDsGA',
    }

    headers = {
        'authority': 'api-service.chanmama.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://www.chanmama.com',
        'pragma': 'no-cache',
        'referer': 'https://www.chanmama.com/liveRank/blogger?category_id=-1&dateType=day&day=2023-04-19',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-client-id': '3020302875',
    }

    params = {
        'day_type': 'day',
        'day': '2023-04-19',
        'category_id': '-1',
        'sort': 'sales_volume',
        'page': '1',
        'size': '50',
        'verification_type': '',
        'is_brand_self_author': '0',
        'is_shop_author': '0',
        'dark_horse': '0',
        'first_rank': '0',
        'is_bomb': '0',
    }

    response = requests.get(
        'https://api-service.chanmama.com/v5/douyin/live/rank/author/sales',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.json()


def get_product_new_data_chart():
    cookies = {
        'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImFwcFZlcnNpb24iOiIiLCJleHBpcmVfdGltZSI6MTY4MjYyMjAwMCwiaWF0IjoxNjgyMDQzNTYwLCJpZCI6MTc0OTM1NywicmsiOiJtanVEdyJ9.PFdlglOq_2BZ2qo4Fw6pZP0hxmgO2gTupf0JOsDZ0E4',
    }

    headers = {
        'authority': 'api-service.chanmama.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://www.chanmama.com',
        'pragma': 'no-cache',
        'referer': 'https://www.chanmama.com/promotionDetail/QqvVTfBpm4SY10xKy5iazjYM2nzlpZhL',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-client-id': '1115190928',
    }

    params = {
        'volume': '1',
        'promotion_id': 'QqvVTfBpm4SY10xKy5iazjYM2nzlpZhL',
        'start_date': '2023-03-22',
        'end_date': '2023-04-20',
    }

    response = requests.get(
        'https://api-service.chanmama.com/v1/product/new/dataChart',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    content = response.json()
    result = decryption(content['data']['data'])
    return result


if __name__ == "__main__":
    pass
