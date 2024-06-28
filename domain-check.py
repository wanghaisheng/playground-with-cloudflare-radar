import aiohttp
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def aiohttp_session(url):
    async with aiohttp.ClientSession() as session:
        yield session

async def test_proxy(test_url,proxy_url):
    try:
        async with aiohttp_session(test_url) as session:
            # Determine the type of proxy and prepare the appropriate proxy header

            # Make the request




            async with session.post(test_url, timeout=10, proxy=proxy_url) as response:
                print(response.status)
                if response.status == 200:
                    headers = response.headers
                    # 获取 "Report-To" 头的值
                    report_to = headers.get('Report-To')
                    

                    print(await response.json())
                    url='https://radar.cloudflare.com/charts/DomainInfoPanel/fetch?domain=woy.ai'

                    headers = {'Report-To': report_to}




                    async with session.get(url, timeout=10, proxy=proxy_url) as response:
                        print(response.status)
                        if response.status == 200:

                            # outfile.add_data(proxy_url)  # Uncomment and replace with your actual implementation
                            return response
                        else:

                            return False
                



                    # outfile.add_data(proxy_url)  # Uncomment and replace with your actual implementation
                    return response
                else:

                    return False
                

            
    except asyncio.TimeoutError:
        # print(f"{Style.BRIGHT}{Color.red}Invalid Proxy (Timeout) | {proxy_url}{Style.RESET_ALL}")
        return False
    except aiohttp.ClientError:

        return False


url='https://radar.cloudflare.com/domains/domain/woy.ai'
url='https://radar.cloudflare.com/charts/DomainInfoPanel/fetch?domain=woy.ai'


asyncio.run(test_proxy(test_url=url,proxy_url=None))           
