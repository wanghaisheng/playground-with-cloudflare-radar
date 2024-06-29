import aiohttp
import asyncio
import json
import base64
from urllib.parse import urlencode,quote

# Target URL for the POST request
url = 'https://radar.cloudflare.com/scan'

# Define the payload with the specified parameters
payload = {
    "url": "https://toolify.ai/",
    "visibility": "Public",
    "customHeaders": {},
    "screenshotsResolutions": ["desktop", "mobile", "tablet"]
}

# Convert the payload to a JSON string, then to a base64 encoded string
payload_json = json.dumps(payload)
payload_b64 = base64.urlsafe_b64encode(payload_json.encode('utf-8')).decode('utf-8')
# print(payload_b64)

# Convert the payload dictionary to a JSON string
payload_url= urlencode(payload)
# print(payload_url)

# URL-encode the JSON string
# payload_target ='body=%7B%22url%22%3A%22https%3A%2F%2Ftoolify.ai%2F%22%2C%22visibility%22%3A%22Public%22%2C%22customHeaders%22%3A%7B%7D%2C%22screenshotsResolutions%22%3A%5B%22desktop%22%2C%22mobile%22%2C%22tablet%22%5D%7D'

encoded_str = "body="+quote(payload_json)

# The result is a URL-encoded JSON string
print(f"{encoded_str}")
# Provided cookie string
cookie_string = '__cf_logged_in=1; CF_VERIFIED_DEVICE_5de93330ab60f42754eeebf5f63f2ed983f6a0280ef2651ec33eaa69e0c64434=1719217177; cf_clearance=BSt1r2ugBL3jAsqKe2ArIOM1uTdGPjCSulEiL6FIymw-1719553423-1.0.1.1-xjyDRT0HXbN.gEhhRL1HcBwqjUBpHodqxKTWd6V.uucfC.kGCIl_2dRGkyozA1978ncgllW5IN4QJqIMKe0E.A; _mkto_trk=id:713-XSC-918&token:_mch-cloudflare.com-1719555178948-38291; _gcl_au=1.1.559844338.1719555181; _biz_uid=77e43d4cd5a24350a064b4cf9a8982f4; cfz_facebook-pixel=%7B%22OwdI_fb-pixel%22%3A%7B%22v%22%3A%22fb.2.1719594043172.2134356791%22%2C%22e%22%3A1751130043172%7D%2C%22VVgx_fb-pixel%22%3A%7B%22v%22%3A%22fb.2.1719594043172.1192340077%22%2C%22e%22%3A1751130043172%7D%2C%22elKW_fb-pixel%22%3A%7B%22v%22%3A%22fb.2.1719594043172.1998253855%22%2C%22e%22%3A1751130043172%7D%7D; cfmrk_cic={"id":"iSk2UptVJM04chv991127dsXSI6IYg21","v1":0,"v2":0,"v3":0,"v5":0,"v7":0,"v8":0,"v6":0}; _ga=GA1.2.613461025.1719594045; _gid=GA1.2.436785959.1719594045; __q_state_37pXYrro6wCZbsU7=eyJ1dWlkIjoiMWEwZDVlZDEtMmVjZC00OWFlLTliNGQtN2NkZWRjYzNiZDFmIiwiY29va2llRG9tYWluIjoiY2xvdWRmbGFyZS5jb20iLCJtZXNzZW5nZXJFeHBhbmRlZCI6ZmFsc2UsInByb21wdERpc21pc3NlZCI6ZmFsc2UsImNvbnZlcnNhdGlvbklkIjoiMTQyODExMTc2MzkyMzE1ODQ2OCJ9; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _biz_nA=4; _biz_pendingA=%5B%5D; cfz_reddit=%7B%22fZaD_reddit_uuid%22%3A%7B%22v%22%3A%221719594114923.c082246f-1f4a-4469-87a2-9d27ed10eca2%22%2C%22e%22%3A1751130114923%7D%7D; cfz_google-analytics_v4=%7B%22nzcr_engagementDuration%22%3A%7B%22v%22%3A%223707%22%2C%22e%22%3A1751130121849%7D%2C%22nzcr_engagementStart%22%3A%7B%22v%22%3A%221719594121849%22%2C%22e%22%3A1751130121849%7D%2C%22nzcr_counter%22%3A%7B%22v%22%3A%2212%22%2C%22e%22%3A1751130114923%7D%2C%22nzcr_session_counter%22%3A%7B%22v%22%3A%222%22%2C%22e%22%3A1751130114923%7D%2C%22nzcr_ga4%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751130114923%7D%2C%22nzcr__z_ga_audiences%22%3A%7B%22v%22%3A%2256a89d4c-0d20-452b-b476-f03719036d2d%22%2C%22e%22%3A1751091172967%7D%2C%22nzcr_let%22%3A%7B%22v%22%3A%221719594114923%22%2C%22e%22%3A1751130114923%7D%7D'
# Split the string into individual cookies
cookies_list = cookie_string.split(';')

# Create a dictionary from the list of cookies
cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_list}

# Convert the dictionary to a JSON string
cookies_json = json.dumps(cookies_dict)
print(cookies_json)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    # Uncomment and add your cookies here if necessary
    'Cookie': cookies_json,
}


encoded_url='https://radar.cloudflare.com/scan?index=&_data=routes%2Fscan%2Findex'
# Asynchronous function to make the POST request
async def make_post_request():
    # Create an aiohttp ClientSession
    async with aiohttp.ClientSession(headers=headers) as session:
        # Make a POST request with the base64 encoded payload
        async with session.post(encoded_url, data=encoded_str) as response:
            # Read and decode the response text
            response_text = await response.text()
            # Print the response text (or process it as needed)
            print(response_text)
# https://radar.cloudflare.com/api/url-scanner/85429445-aa9f-4954-8d52-5b3653b5b01d/screenshot?resolution=desktop
# Run the asynchronous function using asyncio
if __name__ == '__main__':
    asyncio.run(make_post_request())
