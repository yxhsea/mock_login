# 一文教你从零开始入门蝉妈妈数据爬取，成功逆向破解数据加密算法

## 通过接口进行模拟登录

我们先通过正常登录的方式，分析对应的登录接口。通过 F12 打开谷歌浏览器的调试面板，可以看到登录需要传递的一些参数；其中看到密码是被加密了。
![img.png](./images/img.png)

![img_1.png](./images/img_1.png)

不过我们通过经验可以大概猜测一下，应该是通过 md5 算法加密了。
接下来，我们通过 python 来试着调用一下登录接口。
```python
headers = {}

# 将密码通过 md5 加密
password = "xxxxxxxxx"
md5_hash = hashlib.md5()
md5_hash.update(password.encode())
hex_digest = md5_hash.hexdigest()

json_data = {
    'from_platform': None,
    'appId': 10000,
    'timeStamp': 1681976003,
    'username': '13xxxxxxxx7',
    'password': hex_digest
}

response = requests.post('https://api-service.chanmama.com/v1/access/token', headers=headers, json=json_data)
print(response.json())
```

接口返回了正常数据，说明已经登录成功了。
返回的结果里面包含了 token，这个是后续调用其他接口的凭证。
```python
{
	'data': {
		'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImFwcFZlcnNpb24iOiIiLCJleHBpcmVfdGltZSI6MTY4MjYyMjAwMCwiaWF0IjoxNjgyMDQ1MDIwLCJpZCI6MTc0OTM1NywicmsiOiJnMEM3SiJ9.Xf9HaIqszCmZXyT7I0GnKIESfwsw13to7qfVOZJDsGA',
		'expire_time': 1682622000,
		'setting_password': False,
		'activity': '',
		'user_id': 1749357,
		'logged_in': True,
		'is_register': False
	},
	'errCode': 0,
	'rid': '7a45e2061688f182a5495f9549f5e10f'
}
```

## 通过 Token 来爬取数据

使用上面获取到的 token，我们来调用一下其他的接口；这里我们获取一下达人销量排行榜。
```python
cookies = {
    'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImFwcFZlcnNpb24iOiIiLCJleHBpcmVfdGltZSI6MTY4MjUzNTYwMCwiaWF0IjoxNjgxOTc2NjI2LCJpZCI6MTc0OTM1NywicmsiOiI3ZUgzRCJ9.JC5rPXromeZqouDEQIBI6arZb6PIrrL4UkJeMnDRVcI',
}

headers = {}

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
print(response.json())
```

通过返回的结果，证明了通过上面的 token 可以获取到正常的数据。
```python
{
	'rid': 'd92d8085697f1a3eb6968ed552f44ded',
	'data': {
		'list': [{
			'live_room_id': 'GMMn8VDmkc5DRiFgMRxw4V5NYTi0GMEq',
			'unique_id': 'liuyuanyuan1991',
			'follower_count': 16119176,
			'live_show_count': 2,
			'verification_type': 1,
			'sales_volume': 0,
			'avatar': 'https://cdn-images.chanmama.com/douyin/avatar/34e460246d001686558fd71c6913b7ad.jpeg?source=https%3A%2F%2Fp3.douyinpic.com%2Faweme-avatar%2Ftos-cn-avt-0015_cafb3db5654fb4bd4ee700344dba55f7~tplv-dy-shrink%3A188%3A188.jpeg%3Ffrom%3D2956013662',
			'label': '科技数码',
			'sales': 0,
			'room_id': '',
			'rank': 1,
			'day_avg_gmv30': 0,
			'author_step_status': 2,
			'is_black': 0,
			'sales_text': '10w~25w',
			'sales_volume_text': '1000w~2500w',
			'live_room_status': 4,
			'author_id': '21609074922667',
			'nickname': '刘媛媛  22号早9点世界图书日超大活动',
			'product_category': '家居家纺',
			'average_price': 212.67,
			'id': '2023041921609074922667',
			'batch_time': 0
		}],
		'page_info': {
			'page': 1,
			'totalCount': 1500,
			'totalPage': 30,
			'size': 50
		},
		'author_current_index': -1
	},
	'errCode': 0,
	'extraData': {
		'date': '2023-04-19',
		'date_timestamp': 1682035200,
		'msg': '',
		'msg_empty': ''
	}
}
```

## 破解接口加密的数据

但是，蝉妈妈数据有些重要的数据是被加密了的；它是在服务端将要返回的数据加密了，防止在被爬虫直接获取。增强了爬虫的难度。
![img_2.png](./images/img_2.png)
```python
cookies = {
    'LOGIN-TOKEN-FORSNS': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MTAwMDAsImFwcFZlcnNpb24iOiIiLCJleHBpcmVfdGltZSI6MTY4MjYyMjAwMCwiaWF0IjoxNjgyMDQzNTYwLCJpZCI6MTc0OTM1NywicmsiOiJtanVEdyJ9.PFdlglOq_2BZ2qo4Fw6pZP0hxmgO2gTupf0JOsDZ0E4',
}

headers = {
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
print(response.json())
```

返回的加密数据。
```python
{
    "data": {
        "is_encrypt": true,
        "data": "6wvx0lw4suaoJzv8D4XABuyPdWlRQOHiyiPbHFRISY7qIbJuXpjKpeEVs8YGsSLuXs2uwz+RJSM1TR9OxwQjPJsNnvKYfGsE+MKZlqC/3sPi390V8hmPBYuCq9voYxQfh6EBURKgV25hZkdxo7ccADDQRmsONMu0EyJ3xw6sMxyGYYnhUcY+Qr34N4tbWceZKOswcPLHUnMPnncagFGuDBWpSoldtPAAfDtRm4L5F+cgqv0T+slGigB2A0uihnpOJs/2oEBpiSS05C1RaMJmWPMRhCFEtY1/SeaLI/1GSIftPQEuv0YsXL0KeB8Da110R5cFYCA8fFW/zZ4a6Iz6ZchLup6yJ7gMTL1Gn7H30kFIBWZSgvmYaQqmdVJfT4EcbOqhbMMf8V/oaBCaoEnNycpDpbyd8E8WAEIF8S1UUm6Ry+CHlHSleaRfEXqcL1UFxBJtB2U1kzNHlE0MKrN/9oAP16c/90J2HV3imIZYR8y4LE+kIfLNJoHqXyICf/2YOsBsgo8kVi5oU5lVMmxhnHWc0QLPtDJPb/PjSWODghTARNz9QY4MIcsPAiupC0Hayzl11mx1VGg+9fHblKpZcw6Ti7AhUusYXi0qP5wo+ToMLs1u3gXKfrkg8Dgbn/xqu1E/iUHNLenT1glVtIFwb1ZoWFBxZhpv2F8ETXlzzmCZduCAuOnZEk9l06OLCUCkOZXcxQQg9Q269WF8KoqiyCsCFHKEAamNv588rnZj3/ipidOp/BKbMOwwewqnvR6nCczKljQsXfXO77A5GqCV9iwd+ZzacmC9vayxxL9XQSz2BC9HqPiiOWLy0M8osCbXSPGUIGoLwXiE/RVlwEn5T5cIOcK6dfTJJZM26IlC5qw="
    },
    "errCode": 0,
    "rid": "59ff22417f69db96dfafae7374909777"
}
```

从理论上来讲，客户端肯定存在解密的算法；不然，无法将数据展示在界面上。
我们经过不断地打断点进行调试，层层剖析，终于找到数据解密的方法。
可以看到解密算法是使用的 AES 算法，然后再通过 unzip 解压出来。
![img_3.png](./images/img_3.png)

好，到这里，我们再通过 python 代码来还原解密算法。但是，在使用 python 还原解密算法时，出现了一些意想不到的问题；
所有最后，使用 python + js 的方式来实现最终的解密。

```python
def decryption(content):
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


content = "K1QBiIeXQbeXJpvQ8DnuTY5sN/ZO0rpgitVoz4mxYmX01ULj+dBRNeGD1mraDNtehThwSDMMqf0K4WmR6aVXRTDW0zu0BK3NFJYgqmPGv9+E4y8isw2eMVlE+Uyad9lbic14emX1J0fQi33A0LmChi+l7aHqIe/peoRdP5vOUQKs2pyKP3i+ZHRhk3omYnKOlFzQLwXsyXlK6oT6imPtG5zh9Am8ViwPmQRB0UOG/aFnospKEvJL0ndtXlZ7EohXPA2bBBX0rrJ2KDcbm5KOfL0grLIuCIGNeqiZxj52WcFoufrAUc7Gwkx2fTAstkgllzodjydwXQIaiX4rECVuBqsp4uc1E9pJr7KChxY5geDtwFvBGZBtSX2V5CtNgHWONWDp6DBFMULKjr/dKZaG+NfXBx1t0Vid/UOhmGOKjXisT7BRDhDe11Fn1mYJBaEQxuCn1sBWI+2VNJg0qq3ia4+Gw57l9mCvPIGFvS90nPwvyw3QfBRiOdAFjcsuQX8o8PPqm0mhlo7qUfmzido7akZSRRQA+0HMbzzxQs3jTYOe/bW6988hRLg+PhOMBYhwmwe4v4tKzq2kjpcaxyk+DvUv1zg7hIXFQHJFXPFBkSCunfrWxBhWhUDocJ/e+QkqfADsWUK03/L58SpVbIGw5T8Z1YVu5NJ37yt57+sLE3tTO1LLrJTEFshOC8EYxGmDgdhn9ePe40W3ouqRcyulf2oweWaQ4rVC6MutlZBxTjw0Q1e6H+S1X1l98k6jFBW/FG3PHuVCnc/rgHSP5JqBFW5TDJWGfdXndUQRwkLtVGjQkMCY6bI0ZXNzfvfrPHFiXukxh50BMZ71P5MaPvgTvgVa4EtUoJ9erjLRquV9Vb4="
res = decryption(content)
print(res)
```

最终，解密出来的数据。
```python
[{'time_node': 1679414400, 'amount': 0, 'related_author': 0, 'related_live': 0, 'related_aweme': 0, 'volume': 0, 'view_count': 0, 'volume_text': '0', 'amount_text': '0'}, {'related_aweme': 0, 'volume_text': '0', 'amount_text': '0', 'related_live': 0, 'volume': 0, 'amount': 0, 'view_count': 0, 'related_author': 0, 'time_node': 1679500800}, {'amount': 0, 'related_author': 0, 'related_aweme': 0, 'volume_text': '0', 'amount_text': '0', 'time_node': 1679587200, 'volume': 0, 'view_count': 0, 'related_live': 0}, {'time_node': 1679673600, 'view_count': 0, 'related_live': 0, 'amount_text': '0', 'volume': 0, 'amount': 0, 'related_author': 0, 'related_aweme': 0, 'volume_text': '0'}, {'amount': 0, 'related_live': 0, 'related_aweme': 0, 'time_node': 1679760000, 'volume': 0, 'view_count': 0, 'related_author': 0, 'volume_text': '0', 'amount_text': '0'}, {'time_node': 1679846400, 'amount': 0, 'related_live': 0, 'related_aweme': 0, 'volume': 0, 'view_count': 0, 'related_author': 0, 'volume_text': '0', 'amount_text': '0'}, {'related_aweme': 0, 'volume_text': '0', 'amount': 0, 'view_count': 0, 'related_author': 0, 'related_live': 0, 'time_node': 1679932800, 'volume': 0, 'amount_text': '0'}, {'volume': 0, 'amount': 0, 'related_author': 0, 'related_aweme': 0, 'amount_text': '0', 'time_node': 1680019200, 'view_count': 0, 'related_live': 0, 'volume_text': '0'}, {'volume_text': '0', 'amount_text': '0', 'time_node': 1680105600, 'amount': 0, 'view_count': 0, 'related_author': 0, 'volume': 0, 'related_live': 0, 'related_aweme': 0}, {'related_author': 0, 'related_live': 0, 'related_aweme': 0, 'volume_text': '0', 'amount_text': '0', 'view_count': 0, 'volume': 0, 'amount': 0, 'time_node': 1680192000}, {'related_live': 0, 'volume_text': '0', 'amount_text': '0', 'time_node': 1680278400, 'volume': 0, 'amount': 0, 'view_count': 0, 'related_author': 0, 'related_aweme': 0}, {'related_author': 0, 'related_aweme': 0, 'volume': 0, 'view_count': 0, 'related_live': 0, 'volume_text': '0', 'amount_text': '0', 'time_node': 1680364800, 'amount': 0}, {'view_count': 0, 'related_author': 0, 'related_live': 0, 'volume_text': '0', 'amount_text': '0', 'time_node': 1680451200, 'volume': 0, 'amount': 0, 'related_aweme': 0}, {'related_aweme': 0, 'time_node': 1680537600, 'volume': 0, 'view_count': 0, 'related_author': 0, 'related_live': 0, 'amount': 0, 'volume_text': '0', 'amount_text': '0'}, {'related_live': 0, 'related_aweme': 0, 'amount_text': '0', 'time_node': 1680624000, 'volume': 0, 'amount': 0, 'view_count': 0, 'related_author': 0, 'volume_text': '0'}, {'volume': 0, 'related_author': 0, 'related_live': 0, 'time_node': 1680710400, 'amount': 0, 'view_count': 0, 'related_aweme': 0, 'volume_text': '0', 'amount_text': '0'}, {'related_author': 0, 'amount_text': '0', 'view_count': 0, 'related_live': 0, 'related_aweme': 0, 'volume_text': '2500~5000', 'time_node': 1680796800, 'volume': 4500, 'amount': 0}, {'time_node': 1680883200, 'amount': 0, 'view_count': 0, 'related_author': 0, 'volume_text': '1000~2500', 'amount_text': '0', 'volume': 2400, 'related_live': 0, 'related_aweme': 0}, {'volume_text': '1000~2500', 'time_node': 1680969600, 'volume': 1237, 'amount': 0, 'view_count': 0, 'related_author': 0, 'related_live': 0, 'related_aweme': 0, 'amount_text': '0'}, {'related_author': 0, 'related_live': 0, 'volume_text': '500~750', 'amount_text': '0', 'time_node': 1681056000, 'amount': 0, 'view_count': 0, 'related_aweme': 0, 'volume': 543}, {'volume': 76650, 'view_count': 0, 'related_author': 0, 'related_aweme': 0, 'volume_text': '7.5w~10w', 'amount_text': '0', 'time_node': 1681142400, 'amount': 0, 'related_live': 0}, {'related_live': 0, 'volume_text': '10w~25w', 'amount_text': '0', 'view_count': 0, 'related_author': 0, 'related_aweme': 0, 'time_node': 1681228800, 'volume': 100050, 'amount': 0}, {'amount_text': '0', 'amount': 0, 'related_live': 0, 'related_aweme': 0, 'related_author': 0, 'volume_text': '10w~25w', 'time_node': 1681315200, 'volume': 126750, 'view_count': 0}, {'amount': 0, 'related_author': 0, 'related_live': 0, 'volume_text': '25w~50w', 'amount_text': '0', 'volume': 476100, 'view_count': 0, 'related_aweme': 0, 'time_node': 1681401600}, {'volume': 713242, 'amount': 0, 'related_author': 0, 'related_aweme': 0, 'amount_text': '0', 'time_node': 1681488000, 'view_count': 0, 'related_live': 0, 'volume_text': '50w~75w'}, {'amount_text': '0', 'volume': 436035, 'amount': 0, 'related_live': 0, 'related_aweme': 0, 'time_node': 1681574400, 'view_count': 0, 'related_author': 0, 'volume_text': '25w~50w'}, {'amount_text': '0', 'amount': 0, 'view_count': 0, 'related_author': 0, 'related_live': 0, 'time_node': 1681660800, 'volume': 946799, 'related_aweme': 0, 'volume_text': '75w~100w'}, {'related_author': 0, 'volume_text': '100w~250w', 'amount_text': '0', 'time_node': 1681747200, 'volume': 1293041, 'related_live': 0, 'related_aweme': 0, 'amount': 0, 'view_count': 0}, {'volume': 786724, 'amount': 0, 'related_aweme': 0, 'volume_text': '75w~100w', 'amount_text': '0', 'time_node': 1681833600, 'view_count': 0, 'related_author': 0, 'related_live': 0}, {'volume_text': '75w~100w', 'amount_text': '0', 'related_aweme': 0, 'volume': 908524, 'amount': 0, 'view_count': 0, 'related_author': 0, 'related_live': 0, 'time_node': 1681920000}]
```

## 小结
- 首先通过分析登录接口，来实现模拟登录；并且成功获取到接口的调用凭证 Token。
- 使用 Token 也成功的爬取到了其他接口的数据。
- 针对部分接口数据被加密的情况，我们通过层层分析 js 代码；也成功的逆向破解了。
- 最后，声明本篇文章仅供学习参考，网络不是法外之地，切勿进行非法用途。
