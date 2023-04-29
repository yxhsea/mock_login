# 有米有数

有米有数数据的 API 接口，使用的是一种 API 查询语言 graphql。所有的 API 只有一个入口，具体的操作隐藏在请求数据体里面传输。
![img.png](./images/img.png)

## 模拟登录，获取 sessionId

调用登录接口，进行模拟登录。
![img_1.png](./images/img_1.png)

```python
cookies = {}
headers = {}
json_data = {
    'operationName': 'userLogin',
    'query': 'mutation userLogin(\n        $account: String!\n        $password: String!\n        $appId: String\n        $goto: String\n        $riskData: JSON\n        $keep_login: Int\n        $confirm_agreement: Int\n        $params: JSON\n    ) {\n        login(\n            account: $account\n            password: $password\n            appId: $appId\n            goto: $goto\n            riskData: $riskData\n            keep_login: $keep_login\n            confirm_agreement: $confirm_agreement\n            params: $params\n        ) {\n            \n    user {\n        user_id\n        mobile\n        email\n        wx_union_id\n        mobile_verified\n        email_verified\n        register_at\n        extendInfo {\n            industry\n            duty\n            company\n            contact_name\n            wx_nickname\n            avatar\n        }\n    }\n\n            goto\n        }\n    }',
    'variables': {
        'keep_login': 1,
        'account': 'xxx',
        'password': 'xxx',
        'params': {
            'app_id': '',
            'goto': 'https://finance.youcloud.com/account/password',
        },
        'appId': '',
        'goto': 'https://finance.youcloud.com/account/password',
    },
}

response = requests.post('https://api-auth.youcloud.com/graphql', cookies=cookies, headers=headers, json=json_data)
print(response.cookies.items())
```

从 Cookie 数据中，获取到的 sessionId。
```python
[('sessionId', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiI5SDVNMFI3TEFGMVdVNjQ0NWYwYTY4YzZhZiIsImV4cCI6MTY4NDg5NzE5MCwic3ViIjoiNzY4MDY4In0.JeVFFbkIQxe60SwBGqBj93q13OP5ZtA8vC__9ymQwf_wOxfIxooiD4n5TMRPWjRl8ITnHlAEEDxttCxCZ4z8ww')]
```

## 爬取商品列表数据

将上面获取到的 sessionId，应用到其他接口；这里调用商品列表接口。
![img_2.png](./images/img_2.png)

```python
cookies = {
    'sessionId': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiJZMzBEMzM1OU4yUjJBNjQ0M2EwNmVjYmQxYyIsImV4cCI6MTY4NDc0NTU4Miwic3ViIjoiNzY4MDY4In0.li3sxOomDNH7fiA06uMDmLn4cjAZRPWHwx9liHD3yT4iitbAv4EkIFohoHr1o3_CmrZzTPtuB-hq3EJsc0njfQ',
}

headers = {}

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
print(response.json())
```

返回的数据结果，这里只展示部分数据。
```
{
	'data': {
		'productRealTimeList': {
			'data': [{
				'product': {
					'id': 'wlI57Tgth3VaIt6gNOKwfAU=',
					'category': [{
						'id': '110',
						'name': '食品饮料'
					}, {
						'id': '11002',
						'name': '休闲食品'
					}, {
						'id': '1100203',
						'name': '饼干蛋糕'
					}, {
						'id': '1100203041',
						'name': '传统糕点'
					}],
					'header_image': {
						'path': 'https://lp-ag.umcdn.cn/5414a5c887fe3848a70068b22bd438f2/material.jpeg?x-oss-process=image/resize,m_lfit,w_552/quality,Q_80/format,jpg/interlace,1/watermark,size_16,text_5oqW5bqX,shadow_0,t_80,x_16,y_8,color_ffffff,g_sw/watermark,size_16,text_5oqW5bqX,shadow_0,t_80,x_16,y_8,color_212329,g_se'
					},
					'url': 'https://link.youcloud.com?app_id=youshu&goto=https%3A%2F%2Fhaohuo.jinritemai.com%2Fviews%2Fproduct%2Fdetail%3Fid%3D3609573286356382944',
					'title': '【9.9元150包】宣美乐小麻花香酥可口休闲解馋零食六种口味混合',
					'price': '9.9',
					'site': {
						'id': '10502',
						'name': '抖店',
						'icon': 'dd'
					},
					'shop': {
						'id': 'wlI57Tgth3Vat2sz_laEd3I=',
						'name': '宣美樂食品旗舰店',
						'qualification_url': 'https://link.youcloud.com?app_id=youshu&goto=https%3A%2F%2Flb.jinritemai.com%2FshopQualification%3FshopId%3DMIjPNXI%26shopName%3D%E5%AE%A3%E7%BE%8E%E6%A8%82%E9%A3%9F%E5%93%81%E6%97%97%E8%88%B0%E5%BA%97',
						'dsr': '4.82',
						'has_brand': '0',
						'talent': {
							'uid': '4363307679752784',
							'avatar_url': 'https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_9b49ae8d11db430bb8815416f7a0f286.jpeg?from=116350172',
							'nickname': '宣美樂食品旗舰店',
							'track_url': '/kol/4363307679752784/overview'
						}
					},
					'seller_company': {
						'id': '',
						'screenName': '-'
					},
					'first_monitor_time': '2023.04.07 16:15',
					'modify_time': '2023.04.24 10:34',
					'isNew': False
				},
				'promotionType': [{
					'id': '1',
					'name': '广告',
					'shortName': '广告'
				}, {
					'id': '3',
					'name': '直播',
					'shortName': '直播'
				}],
				'measureValue': '1,000',
				'qs_incr_24h': '232.81万',
				'qs_incr_24h_ratio': '-23%',
				'qs_incr_12h': '65.29万',
				'qs_incr_6h': '17.07万',
				'qs_incr_3h': '11.73万',
				'qs_incr_1h': '6.88万',
				'qs_amount_incr': '2409.26万',
				'qs_total': '2126.82万'
			}],
				'measureValue': '1,000',
				'qs_incr_24h': '37.76万',
				'qs_incr_24h_ratio': '-7%',
				'qs_incr_12h': '14.25万',
				'qs_incr_6h': '6.51万',
				'qs_incr_3h': '4.98万',
				'qs_incr_1h': '2.97万',
				'qs_amount_incr': '462.52万',
				'qs_total': '312.04万'
		],
			'total': 1487478,
			'limit': 20
		}
	}
}
```

## 小结
- 有米有数数据接口使用的是 graphql 查询语言。
- 调用登录接口，获取到 sessionId。
- 使用 sessionId 便可以爬取到商品数据。
- 最后，声明本篇文章仅供学习参考，网络不是法外之地，切勿进行非法用途