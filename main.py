import asyncio
from aiohttp import request
from aiomultiprocess import Pool
import aiodns

async def get(url):
    async with request("GET", url) as response:
        return await response.text("utf-8")
URLS = []
# 读取域名
def read_domain():
    global URLS
    with open ('subdomain.txt') as domains:
        for domain in domains:
            URLS.append(domain.split('\n')[0])
            print(URLS)
# 获取CNAME记录
async def cname_get(subdomain):
    resolver = aiodns.DNSResolver(timeout=2)
    try:
        result = await resolver.query(subdomain,'CNAME')
        return subdomain,result
    except:
        pass
async def main():
    async with Pool() as pool:
        result = await pool.map(cname_get, URLS)
        print(result[1])
if __name__ == '__main__':
    read_domain()
    asyncio.run(main())