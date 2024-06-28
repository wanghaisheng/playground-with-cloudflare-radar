import aiohttp
import asyncio
import json

# 请求的URL，注意对URL参数进行URL编码
url = 'https://radar.cloudflare.com/api/search?query=https%3A%2F%2Fwoy.ai%2F'

async def fetch_cloudflare_radar_data(url):
    # 请求头，包括站点策略
    headers = {
        'Referer': 'https://radar.cloudflare.com/api/search?query=https%3A%2F%2Fwoy.ai%2F',
        'Report-To': 'same-origin'  ,# 引用站点策略,
        'Content-type':"application/x-www-form-urlencoded;charset=UTF-8",
            'Cookie':"__cf_logged_in=1; CF_VERIFIED_DEVICE_5de93330ab60f42754eeebf5f63f2ed983f6a0280ef2651ec33eaa69e0c64434=1719217177; cf_clearance=BSt1r2ugBL3jAsqKe2ArIOM1uTdGPjCSulEiL6FIymw-1719553423-1.0.1.1-xjyDRT0HXbN.gEhhRL1HcBwqjUBpHodqxKTWd6V.uucfC.kGCIl_2dRGkyozA1978ncgllW5IN4QJqIMKe0E.A; cfzs_google-analytics_v4=%7B%22nzcr_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D; _mkto_trk=id:713-XSC-918&token:_mch-cloudflare.com-1719555178948-38291; _gcl_au=1.1.559844338.1719555181; _biz_uid=77e43d4cd5a24350a064b4cf9a8982f4; _biz_nA=2; _biz_pendingA=%5B%5D; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%7D; __cf_bm=34IWY2xq6koB_TWGABGf8e9wxaBA3LV9NnfhpJeRXyE-1719556522-1.0.1.1-6mB2f5V.Dr4ftLIi1z3tvmTFgjvCkLU8bEgc3giHP1_z5jD4BkoXFcG_otZruJ5b3zIuavMYv1jG6dbWgCrkgg; cfz_google-analytics_v4=%7B%22nzcr_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_engagementStart%22%3A%7B%22v%22%3A%221719556626809%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_ga4sid%22%3A%7B%22v%22%3A%22337350929%22%2C%22e%22%3A1719558426809%7D%2C%22nzcr_session_counter%22%3A%7B%22v%22%3A%221%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr_ga4%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751092626809%7D%2C%22nzcr__z_ga_audiences%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751091172967%7D%2C%22nzcr_let%22%3A%7B%22v%22%3A%221719556626809%22%2C%22e%22%3A1751092626809%7D%7D"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            # 确保请求成功
            if response.status == 200:
                # 解析JSON格式的响应数据
                response_data = await response.json()
                print("Response Data:", json.dumps(response_data, indent=2))
                return response_data
            else:
                print(f"Failed to get 200 OK status code, status code: {response.status}")

# 运行异步函数
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_cloudflare_radar_data(url))
