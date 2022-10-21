import asyncio
import time
import aiohttp

start_time = time.time()

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
kw_list = ['cat', 'dog', 'mouse']


async def request(data):
    async with aiohttp.ClientSession() as session:
        async with await session.post(url=url, headers=headers, data=data) as response:
            result = await response.json()
            print(result)


tasks = []
for kw in kw_list:
    data = {
        'kw': kw
    }
    c = request(data)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
print(end_time - start_time)
