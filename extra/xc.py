import asyncio
import functools
import time

async def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))

async def main(urls):
    start = time.perf_counter()
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
    end = time.perf_counter()
    print('{} took {} ms'.format(main.__name__, (end - start) * 1000))

asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# main(['url_1','url_2','url_3','url_4'])
# asyncio.run(main(['url_1','url_2','url_3','url_4']))
