#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def product_realtime_list():
    cookies = {
        'sessionId': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiI5SDVNMFI3TEFGMVdVNjQ0NWYwYTY4YzZhZiIsImV4cCI6MTY4NDg5NzE5MCwic3ViIjoiNzY4MDY4In0.JeVFFbkIQxe60SwBGqBj93q13OP5ZtA8vC__9ymQwf_wOxfIxooiD4n5TMRPWjRl8ITnHlAEEDxttCxCZ4z8ww',
    }

    headers = {
        'authority': 'api.youshu.youcloud.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://console.youshu.youcloud.com',
        'pragma': 'no-cache',
        'referer': 'https://console.youshu.youcloud.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-operation-name': 'productRealTimeList',
    }

    json_data = {
        'operationName': 'productRealTimeList',
        'query': '\n        query productRealTimeList (\n            $site_id: String\n            $category: String\n            $promotionType: String\n            $shopType: String\n            $hasBrand: String\n            $min_qs_incr_24h: String\n            $max_qs_incr_24h: String\n            $min_qs_incr_12h: String\n            $max_qs_incr_12h: String\n            $min_qs_incr_6h: String\n            $max_qs_incr_6h: String\n            $min_qs_total: String\n            $max_qs_total: String\n            $min_qs_incr_day: String\n            $max_qs_incr_day: String\n            $min_qs_incr_amount_day: String\n            $max_qs_incr_amount_day: String\n            $page: Int!\n            $sort: ProductListSort!\n            $min_measure: String\n            $max_measure: String\n            $isExport: Boolean!\n        ) {\n            productRealTimeList (\n                site_id: $site_id\n                category: $category\n                promotionType: $promotionType\n                shopType: $shopType\n                hasBrand: $hasBrand\n                min_qs_incr_24h: $min_qs_incr_24h\n                max_qs_incr_24h: $max_qs_incr_24h\n                min_qs_incr_12h: $min_qs_incr_12h\n                max_qs_incr_12h: $max_qs_incr_12h\n                min_qs_incr_6h: $min_qs_incr_6h\n                max_qs_incr_6h: $max_qs_incr_6h\n                min_qs_total: $min_qs_total\n                max_qs_total: $max_qs_total\n                min_qs_incr_day: $min_qs_incr_day\n                max_qs_incr_day: $max_qs_incr_day\n                min_qs_incr_amount_day: $min_qs_incr_amount_day\n                max_qs_incr_amount_day: $max_qs_incr_amount_day\n                sort: $sort\n                page: $page\n                min_measure: $min_measure\n                max_measure: $max_measure\n                isExport: $isExport\n            ) {\n                data {\n                    product {\n                        \n    id @skip(if: $isExport)\n    category @skip(if: $isExport) {\n        \n    id\n    name\n\n    }\n    header_image @skip(if: $isExport) {\n        \n    path\n\n    }\n    url\n    title\n    price\n    site {\n        \n    id\n    name\n    icon\n\n    }\n    shop {\n        \n    id\n    name\n    qualification_url\n    dsr\n\n        has_brand\n        talent {\n            \n    uid\n    avatar_url\n    nickname\n\n            track_url\n        }\n    }\n    seller_company {\n        \n    id\n    screenName\n\n    }\n    first_monitor_time\n    modify_time\n    isNew @skip(if: $isExport)\n\n                    }\n                    promotionType {\n                        \n    id\n    name\n    shortName\n\n                    }\n                    measureValue\n                    qs_incr_24h\n                    qs_incr_24h_ratio\n                    qs_incr_12h\n                    qs_incr_6h\n                    qs_incr_3h\n                    qs_incr_1h\n                    qs_amount_incr\n                    qs_total\n                }\n                total\n                limit\n            }\n        }\n    ',
        'variables': {
            'site_id': '10501',
            'sort': 'qs_incr_24h',
            'page': 1,
            'isExport': False,
        },
    }

    response = requests.post('https://api.youshu.youcloud.com/graphql', cookies=cookies, headers=headers, json=json_data)
    return response.json()


if __name__ == "__main__":
    print(product_realtime_list())
