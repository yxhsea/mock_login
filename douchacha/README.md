# 使用爬虫利器 Playwright，轻松爬取抖查查数据

我们先分析登录的接口，其中 url 有一些非业务参数：ts、he、sign、secret。
![img_6.png](./images/img_6.png)
然后根据这些参数作为关键词，定位到相关的 js 代码。
![img_5.png](./images/img_5.png)
最后，逐步进行代码的跟踪，发现大部分的代码被混淆加密了。
![img_7.png](./images/img_7.png)
花费了大半天，来还原这些混淆加密的代码，但是也没有逆向出来。
走到这里就是个坑了，那没有其他的方法了吗？

我们换个思路，换道超车，使用自动化的方式，通过启动浏览器的方式，模拟用户的行为。
监听相关的网络请求，来拦截数据；虽然这种方式比较的蹩脚，但是也能达到数据爬取的目的。

## 使用 playwright 库实现自动化模拟登录

打开抖查查首页
```python
# 打开抖查查首页
page.goto("https://www.douchacha.com/")
```
![img.png](./images/img.png)

点击登录
```python
# 点击 登录按钮
page.wait_for_timeout(random.randint(2, 5) * 1000)
page.click("xpath=//p[@class=\"login_txt\"]//span[@class=\"login\"]")
```
![img_1.png](./images/img_1.png)

切换到手机号登录模式
```python
page.wait_for_timeout(random.randint(2, 5) * 1000)
page.click("xpath=//a[@class=\"login_dialog_switch\"]")
```
![img_2.png](./images/img_2.png)

填写手机号、密码、点击登录
```python
# 填写 账号、密码
page.wait_for_timeout(random.randint(2, 5) * 1000)
page.fill("xpath=//input[@placeholder=\"请输入手机号\"]", "xxxxxx")
page.fill("xpath=//input[@placeholder=\"请输入密码\"]", "xxxxx")

# 点击 登录
page.wait_for_timeout(random.randint(2, 5) * 1000)
page.click("xpath=//div[@class=\"login_warp\"]//div[@class=\"login_input_warp\"]//button//span[contains(text(), \"登录\")]")
```
![img_3.png](./images/img_3.png)

登录成功之后的 Cookie 数据，这里只展示部分数据。
```python
[{
	"name": "HMACCOUNT_BFESS",
	"value": "4E58BF464182BB65",
	"domain": ".hm.baidu.com",
	"path": "/",
	"expires": 1716691140.784459,
	"httpOnly": false,
	"secure": true,
	"sameSite": "None"
}, {
	"name": "Hm_lvt_5e3b865d73ba569c052e9fb5792de511",
	"value": "1682131141",
	"domain": ".douchacha.com",
	"path": "/",
	"expires": 1713667155,
	"httpOnly": false,
	"secure": false,
	"sameSite": "Lax"
}]
```

## 爬取抖音的商品列表数据

将上面保存下来的 Cookie 数据，应用到其他的页面。
```python
context = browser.new_context()
# 设置 cookie
with open("./cookies.txt", "r") as f:
    cookies = json.loads(f.read())
    context.add_cookies(cookies)
page = context.new_page()
```

打开搜索商品页面
```python
# 打开抖查查商品搜索页面
page.goto("https://www.douchacha.com/searchshopdetail")

# 设置回调函数
page.on('response', response_callback)
```
![img_4.png](./images/img_4.png)

数据回调函数，其实本质就是监听也 network 网络请求，然后进行过滤。
```python
def response_callback(response):
    # 过滤出商品列表接口数据
    if '/api/tiktok/search/goods' in response.url and response.status == 200:
        print(response.json())
```

爬取到的商品数据，这里只展示部分数据。
```python
{
	'code': 200,
	'msg': '',
	'data': {
		'result': [{
			'range_business_total_sales7_new': '200w+',
			'range_business_total_sales30_new': '200w+',
			'range_platform_sales': '0',
			'range_sales': '1000w+',
			'goods_id': '83419cd43abb55e4b6bab118c5ba75a10e25ada76a6e9530dabc307aab72869d',
			'title': '【9.99元150包】宣美乐小麻花香酥可口休闲解馋零食六种口味混合',
			'big_title': '【9.9元150包】宣美乐小麻花香酥可口休闲解馋零食六种口味混合装',
			'image': 'https://p26-item.ecombdimg.com/img/ecom-shop-material/v1_MIjPNXI_71166834225882893150966_fe71d81300602fd5d766f1b1ff74671c_sx_205628_www1022-1022~tplv-5mmsx3fupr-resize:1080:1080.jpeg',
			'sales': '15987150',
			'platform_sales': '0',
			'price': '999',
			'last_update_time': '1682125751327',
			'promotion_id': '3609573447434420470',
			'brand': 'XUANMEILE/宣美樂',
			'business_total_pv': '0',
			'business_total_user': '0',
			'view_count': '36208',
			'coupon_price': 0.0,
			'cos_fee': '150',
			'cos_fee_scale': 0.1505,
			'goods_source': '小店',
			'goods_source_type': 2,
			'market_price': '999',
			'detail_url': 'https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=3609573286356382944&origin_type=2002170010&origin_id=99514375927_3609573447434420470&alkey=1128_99514375927_0_3609573447434420470_011&sec_author_id=MS4wLjABAAAA2I9NdgAKZrz9e0tLm1csyDMNqLESPDm34TdYYqXe8-I&from_link=1&c_biz_combo=2&use_link_command=1&goods_detail=%7B%22title%22%3A%22%E3%80%909.99%E5%85%83150%E5%8C%85%E3%80%91%E5%AE%A3%E7%BE%8E%E4%B9%90%E5%B0%8F%E9%BA%BB%E8%8A%B1%E9%A6%99%E9%85%A5%E5%8F%AF%E5%8F%A3%E4%BC%91%E9%97%B2%E8%A7%A3%E9%A6%8B%E9%9B%B6%E9%A3%9F%E5%85%AD%E7%A7%8D%E5%8F%A3%E5%91%B3%E6%B7%B7%E5%90%88%22%2C%22sales%22%3A15987150%2C%22img%22%3A%7B%22uri%22%3A%22ecom-shop-material%2Fv1_MIjPNXI_71166834225882893150966_fe71d81300602fd5d766f1b1ff74671c_sx_205628_www1022-1022%22%2C%22url_list%22%3A%5B%22https%3A%2F%2Fp3-item.ecombdimg.com%2Fimg%2Fecom-shop-material%2Fv1_MIjPNXI_71166834225882893150966_fe71d81300602fd5d766f1b1ff74671c_sx_205628_www1022-1022~tplv-5mmsx3fupr-image.png%22%2C%22https%3A%2F%2Fp26-item.ecombdimg.com%2Fimg%2Fecom-shop-material%2Fv1_MIjPNXI_71166834225882893150966_fe71d81300602fd5d766f1b1ff74671c_sx_205628_www1022-1022~tplv-5mmsx3fupr-image.png%22%5D%2C%22width%22%3A100%2C%22height%22%3A100%7D%2C%22min_price%22%3A999%2C%22max_price%22%3A999%7D&detail_schema=sslocal%3A%2F%2Fec_goods_detail%3Fpromotion_id%3D3609573447434420470%26product_id%3D3609573286356382944%26item_id%3D0%26kol_id%3D99514375927%26enter_from%3Dcopy%26source_page%3Dcopy%26meta_params%3D%26request_additions%3D%257B%2522from_internal_feed%2522%253A%2522false%2522%252C%2522cps_track%2522%253A%2522%2522%252C%2522marketing_channel%2522%253A%2522%2522%257D&h5_origin_type=detail_share',
			'video_exceptlive': 0.12,
			'live_except_video': 0.88,
			'video_count30': '1183',
			'user_count30': '2187',
			'live_count30': '3880',
			'conversion_rate30': 1.0,
			'video_count7': '1103',
			'user_count7': '2091',
			'live_count7': '3633',
			'video_count_y': '103',
			'user_count_y': '640',
			'live_count_y': '741',
			'business_total_sales7_new': '2288800',
			'live_sales_grow30': '0',
			'video_sales_grow30': '0',
			'goods_video_rate': 0.0,
			'goods_live_rate': 0.0,
			'business_total_sales30_new': '2740500',
			'first_cid': '8',
			'second_cid': '20018',
			'thrid_cid': '20312',
			'shop_id': 'd5e2b4885996eff784d18feca4291b3f',
			'brand_id': '3943caf2696213efef6d630cfe883ce3b4b3a448335aa2b1a75b9ada4f557da2',
			'status': 1,
			'up_status': 1,
			'percent': 89.5306,
			'good_rate': 0.8953068592057761,
			'has_speci': True,
			'range_business_total_sales_y_new': '46w+',
			'business_total_sales_y_new': '466200'
		}],
		'page_no': '1',
		'page_size': '10',
		'total_page': '1564721',
		'total_record': '15647209',
		'show_original_data': False,
		'user_grade': 'FREE',
		'data_max': 10
	}
}
```

## 小结
- 抖查查所有的接口都进行了签名校验，及 js 代码混淆加密，逆向难度高。
- 变换思路，使用 playwright 自动化的方式模拟登录，及接口数据拦截。
- 最终，达到数据爬取的目的；当然，最好的方式是能够反混淆逆向 js 代码。
- 最后，声明本篇文章仅供学习参考，网络不是法外之地，切勿进行非法用途。
