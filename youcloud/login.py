#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def login():
    cookies = {
        '_ga': 'GA1.1.2103187981.1682145247',
        'localeLanguage': 'zh',
        'MEIQIA_TRACK_ID': '2Olpv15LIWKGClck2wEDkDCoiPU',
        'MEIQIA_VISIT_ID': '2OlpuzGzTF6FaZUVrrRo8RnvGgy',
        'openTrialPop': '768068',
        '_ga_SFG2Z62L10': 'GS1.1.1682152988.3.1.1682153051.0.0.0',
        '_ga_QNB91PL4C6': 'GS1.1.1682152947.3.1.1682153078.0.0.0',
        'ph_oEY7uwNI-BrLK7aN1Al8D1-abXKFEeENlm9zn5gOvzM_posthog': '%7B%22distinct_id%22%3A%22768068%22%2C%22%24device_id%22%3A%22187a7ab805b0-08b3502cb335eb-18525635-13c680-187a7ab805c1575%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fauth.youcloud.com%2Flogout%3Fapp_id%3Dyoushu%26goto%3Dhttps%253A%252F%252Fconsole.youshu.youcloud.com%252Fgoods%252FrealtimeSale%22%2C%22%24initial_referring_domain%22%3A%22auth.youcloud.com%22%2C%22%24referrer%22%3A%22https%3A%2F%2Ffinance.youcloud.com%2F%22%2C%22%24referring_domain%22%3A%22finance.youcloud.com%22%2C%22app_release%22%3A%22v1.5.0-youcloud-account%22%2C%22language%22%3A%22zh-CN%22%2C%22document_lang%22%3A%22%22%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24user_id%22%3A%22768068%22%7D',
    }

    headers = {
        'authority': 'api-auth.youcloud.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.1.2103187981.1682145247; localeLanguage=zh; MEIQIA_TRACK_ID=2Olpv15LIWKGClck2wEDkDCoiPU; MEIQIA_VISIT_ID=2OlpuzGzTF6FaZUVrrRo8RnvGgy; openTrialPop=768068; _ga_SFG2Z62L10=GS1.1.1682152988.3.1.1682153051.0.0.0; _ga_QNB91PL4C6=GS1.1.1682152947.3.1.1682153078.0.0.0; ph_oEY7uwNI-BrLK7aN1Al8D1-abXKFEeENlm9zn5gOvzM_posthog=%7B%22distinct_id%22%3A%22768068%22%2C%22%24device_id%22%3A%22187a7ab805b0-08b3502cb335eb-18525635-13c680-187a7ab805c1575%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fauth.youcloud.com%2Flogout%3Fapp_id%3Dyoushu%26goto%3Dhttps%253A%252F%252Fconsole.youshu.youcloud.com%252Fgoods%252FrealtimeSale%22%2C%22%24initial_referring_domain%22%3A%22auth.youcloud.com%22%2C%22%24referrer%22%3A%22https%3A%2F%2Ffinance.youcloud.com%2F%22%2C%22%24referring_domain%22%3A%22finance.youcloud.com%22%2C%22app_release%22%3A%22v1.5.0-youcloud-account%22%2C%22language%22%3A%22zh-CN%22%2C%22document_lang%22%3A%22%22%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24user_id%22%3A%22768068%22%7D',
        'origin': 'https://auth.youcloud.com',
        'pragma': 'no-cache',
        'referer': 'https://auth.youcloud.com/login?app_id=&goto=https%3A%2F%2Ffinance.youcloud.com%2Faccount%2Fpassword',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-operation-name': 'userLogin',
    }

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
    return response.cookies.items()


if __name__ == "__main__":
    print(login())
