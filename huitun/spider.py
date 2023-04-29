#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def search_user():
    cookies = {
        'SESSION': 'NzAyNDQ4MjMtMGMyZS00OTBiLThiMWUtMTNmZWNkMjkxYThh',
    }

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://dy.huitun.com',
        'Pragma': 'no-cache',
        'Referer': 'https://dy.huitun.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        '_t': '1682146378787',
        'cids': '10117',
        'tagList': '',
        'followerRange': '',
        'diggRange': '',
        'ageRange': '',
        'scoreRange': '',
        'gender': '',
        'fansGroup': '',
        'liveGmv': '',
        'province': '',
        'region': '',
        'maxGender': '',
        'maxAge': '',
        'maxArea': '',
        'maxCity': '',
        'customVerify': '',
        'playRange': '',
        'rateRange': '',
        'isEarnest': '',
        'company': '',
        'isOpenWindow': '',
        'hasMcn': '',
        'contactWay': '',
        'isLive': '',
        'goodsSource': '',
        'sales': '',
        'visitorRange': '',
        'prices': '',
        'goodsKeyword': '',
        'keywordMatch': '',
        'goodsCates': '',
        'subIds': '',
        'leafIds': '',
        'keyword': '',
        'from': '1',
        'sortField': '',
        'tag': '0',
        'tryIt': '',
        'cat0': '',
        'cat1': '',
        'maxCg': '',
        'maxCl': '',
        'fusionShopFlag': 'false',
    }

    response = requests.get('https://dyapi.huitun.com/search/user', params=params, cookies=cookies, headers=headers)
    return response.json()


if __name__ == "__main__":
    print(search_user())
