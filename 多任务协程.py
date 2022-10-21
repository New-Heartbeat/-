import time
import asyncio

async def request(url):
    print('正在下载', url)
    # time.sleep(2)
    await asyncio.sleep(2)
    print('下载成功', url)

start = time.time()
url_list = [
    'www.baidu.com',
    'www.sougou.com',
    'www.douyu.com'
]

# 任务列表
tasks = []
for url in url_list:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end - start)


