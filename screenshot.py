import aiohttp
import asyncio
import json

# 请求数据
post_data = {
    "url": "https://woy.ai/",
    "visibility": "Public",
    "customHeaders": {},
    "screenshotsResolutions": ["desktop", "mobile", "tablet"]
}

# 将数据转换为JSON格式的字符串
json_data = json.dumps(post_data)

async def send_post_request(url):
    # 请求头，包括站点策略
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cf-Ray':"89abb1040d688bc6-SIN",
        'Referer': 'https://radar.cloudflare.com/scan?index=&_data=routes%2Fscan%2Findex',
        # 'Report-To': 'same-origin'  # 引用站点策略
        'Cookie':"__cf_logged_in=1; CF_VERIFIED_DEVICE_5de93330ab60f42754eeebf5f63f2ed983f6a0280ef2651ec33eaa69e0c64434=1719217177; cf_clearance=BSt1r2ugBL3jAsqKe2ArIOM1uTdGPjCSulEiL6FIymw-1719553423-1.0.1.1-xjyDRT0HXbN.gEhhRL1HcBwqjUBpHodqxKTWd6V.uucfC.kGCIl_2dRGkyozA1978ncgllW5IN4QJqIMKe0E.A; cfzs_google-analytics_v4=%7B%22nzcr_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D; _mkto_trk=id:713-XSC-918&token:_mch-cloudflare.com-1719555178948-38291; _gcl_au=1.1.559844338.1719555181; _biz_uid=77e43d4cd5a24350a064b4cf9a8982f4; _biz_nA=2; _biz_pendingA=%5B%5D; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%7D; __cf_bm=34IWY2xq6koB_TWGABGf8e9wxaBA3LV9NnfhpJeRXyE-1719556522-1.0.1.1-6mB2f5V.Dr4ftLIi1z3tvmTFgjvCkLU8bEgc3giHP1_z5jD4BkoXFcG_otZruJ5b3zIuavMYv1jG6dbWgCrkgg; cfz_google-analytics_v4=%7B%22nzcr_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_engagementStart%22%3A%7B%22v%22%3A%221719556626809%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_ga4sid%22%3A%7B%22v%22%3A%22337350929%22%2C%22e%22%3A1719558426809%7D%2C%22nzcr_session_counter%22%3A%7B%22v%22%3A%221%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_ga4%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr__z_ga_audiences%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751091172967%7D%2C%22nzcr_let%22%3A%7B%22v%22%3A%221719556626809%22%2C%22e%22%3A1751092626809%7D%7D",
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json_data) as response:
            print(f"Status Code: {response.status}")
            if response.status == 200:
                # 如果状态码是200 OK，打印响应内容
                response_text = await response.text()
                print("Response Text:", response_text)
            else:
                print("Failed to get 200 OK status code.")

# 请求的 URL
url = 'https://radar.cloudflare.com/scan?index=&_data=routes%2Fscan%2Findex'

# 运行异步函数
asyncio.run(send_post_request(url))
