#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import hashlib


def get_access_token():
    headers = {
        'authority': 'api-service.chanmama.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.chanmama.com',
        'pragma': 'no-cache',
        'referer': 'https://www.chanmama.com/login',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-client-id': '3020302875',
    }

    # 将密码通过 md5 加密
    password = "xxxxxx"
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode())
    hex_digest = md5_hash.hexdigest()

    json_data = {
        'from_platform': None,
        'appId': 10000,
        'timeStamp': 1681976003,
        'username': 'xxxxxxxxx',
        'password': hex_digest
    }

    response = requests.post('https://api-service.chanmama.com/v1/access/token', headers=headers, json=json_data)
    return response.json()


if __name__ == "__main__":
    pass
