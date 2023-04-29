#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import execjs
import hashlib
import time


def login():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
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

    phone_num = "xxxx"
    password = "xxxx"
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode())
    hex_digest = md5_hash.hexdigest()

    data = {
        'phoneNum': phone_num,
        'pwd': hex_digest,
        't': int(time.time() * 1000),
        'tenant': 1,
    }

    with open('sign.js', 'r', encoding='UTF-8') as f:
        js_code = f.read()
        context = execjs.compile(js_code)
        sign = context.call("get_sign", data['phoneNum'], data['pwd'], data['t'])
    data['sig'] = sign

    response = requests.post('https://user.hrdjyun.com/wechat/phonePwdLogin', headers=headers, json=data)
    return response.json()


if __name__ == "__main__":
    pass
