#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests
import hashlib


def business_good_search():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://www.hh1024.com',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    token = 'vlkqda3oJMk7TARL+3tsKte1hwyFf4C4+N0X+t4+BAshPm2zjOHV0w=='
    data = {
        'param': '{"no":"dy70000","data":{"name":"","dyCategoryName":"","categoryName":"","priceStart":"","priceEnd":"","salesVolumeStart":"","salesVolumeEnd":"","orderBy":"salesMoney30","order":"desc","pageSize":100,"pageNum":1,"cosRatioStart":""}}',
        'tenant': '1',
        'timestamp': int(time.time() * 1000),
        'token': token,
    }

    sign_str = 'param={}&timestamp={}&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'.format(data['param'], data['timestamp'])
    sign = hashlib.sha256(sign_str.encode('utf-8')).hexdigest()
    data['sign'] = sign

    response = requests.post('https://ucp.hrdjyun.com:60359/api/dy', headers=headers, json=data)
    print(response.json())


if __name__ == "__main__":
    business_good_search()
