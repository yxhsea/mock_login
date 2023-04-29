#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


def get_growing_up_rank():
    with open("cookies.txt", 'r') as f:
        content = f.read()
        cookies = json.loads(content)

    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']

    cookies = cookie_dict

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://dy.feigua.cn/app/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'pageIndex': '1',
        'pageSize': '10',
        'period': 'day',
        'datecode': '20230419',
        '_': '1681972040924',
    }

    response = requests.get('https://dy.feigua.cn/api/v1/bloggerrank/growingUpRank', params=params, cookies=cookies, headers=headers)
    return response.json()


if __name__ == "__main__":
    pass
