# python 协程
'''
    1. asyncio.create_task，asyncio.run 这些函数都是 Python 3.7 以上的版本才提供的，自然，相比于旧接口它们也更容易理解和阅读。
    2. *tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数。
'''

import asyncio
import functools
import random
import time

if __name__ == "__main__":

    # 爬虫的例子
    def log_execution_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            start = time.perf_counter()
            res = func(*args, **kargs)
            end = time.perf_counter()
            print("函数{}运行耗时{}秒".format(func.__name__, end - start))
            return res

        return wrapper

    def crawl_page(url):
        print("正在爬取url = {}".format(url))
        sleep_time = int(url.split('_')[-1])
        time.sleep(sleep_time)
        print("OK {}".format(url))

    @log_execution_time
    def main(urls):
        for url in urls:
            crawl_page(url)

    # main(["url_1", "url_2", "url_3", "url_4"])

    # 并发版爬虫，效果与上面一致
    # 异步函数
    async def crawl_page2(url):
        print("正在爬取{}".format(url))
        sleep_time = int(url.split('_')[-1])
        await asyncio.sleep(sleep_time) # 休眠数秒，
        print("OK {}".format(url))

    async def main2(urls):
        for url in urls:
            await crawl_page2(url) # await是同步调用

    # start = time.perf_counter()
    # asyncio.run(main2(["url_1", "url_2", "url_3", "url_4"]))
    # end = time.perf_counter()
    # print("2运行耗时{}秒".format(end - start))


    # 真正的并发版爬虫
    async def main3(urls):
        tasks = [asyncio.create_task(crawl_page2(url)) for url in urls] # asyncio.create_task创建任务
        for task in tasks:
            await task

    # start = time.perf_counter()
    # asyncio.run(main3(["url_1", "url_2", "url_3", "url_4"])) # 程序进入 main() 函数，事件循环开启
    # end = time.perf_counter()
    # print("3运行耗时{}秒".format(end - start))


    # task的另一种做法
    async def main4(urls):
        tasks = [asyncio.create_task(crawl_page2(url)) for url in urls]
        await asyncio.gather(*tasks)  # *tasks 解包列表，将列表变成了函数的参数


    start = time.perf_counter()
    asyncio.run(main4(["url_1", "url_2", "url_3", "url_4"])) # 程序进入 main() 函数，事件循环开启
    end = time.perf_counter()
    print("3运行耗时{}秒".format(end - start))


    # 协程运行底层
    async def worker_1():
        print("work1开始")
        await asyncio.sleep(1)
        print("work1结束")


    async def worker_2():
        print("work2开始")
        await asyncio.sleep(2)
        print("work2结束")


    async def main5():
        print("await之前")
        await worker_1()
        print("await worker_1之后")
        await worker_2()
        print("await worker_2之后")


    start = time.perf_counter()
    asyncio.run(main5())
    end = time.perf_counter()
    print("5运行耗时{}秒".format(end - start))


    async def main6():
        task1 = asyncio.create_task(worker_1())
        task2 = asyncio.create_task(worker_2())
        print("await之前")
        await task1
        print("await worker_1之后")
        await task2
        print("await worker_2之后")


    start = time.perf_counter()
    asyncio.run(main6())
    end = time.perf_counter()
    print("6运行耗时{}秒".format(end - start))


    # 限定时间，超出就取消。协程出现错误
    async def worker1():
        await asyncio.sleep(1)
        return 1


    async def worker2():
        await asyncio.sleep(2)
        return 2 / 0


    async def worker3():
        await asyncio.sleep(3)
        return 3


    async def main7():
        task1 = asyncio.create_task(worker1())
        task2 = asyncio.create_task(worker2()) # 运行报错 [ZeroDivisionError('division by zero'), ZeroDivisionError('division by zero'), CancelledError('')]
        task3 = asyncio.create_task(worker3()) # 超时取消
        await asyncio.sleep(2)
        task3.cancel()

        res = await asyncio.gather(task2, task2, task3, return_exceptions=True) # return_exceptions=True这行代码。如果不设置这个参数，错误就会完整地 throw 到我们这个执行层，从而需要 try except 来捕捉，这也就意味着其他还没被执行的任务会被全部取消掉。为了避免这个局面，我们将 return_exceptions 设置为 True 即可。
        print(res)


    start = time.perf_counter()
    asyncio.run(main7())
    end = time.perf_counter()
    print("7运行耗时{}秒".format(end - start))


    # 生产者消费者模型
    async def consumer(queue, id):
        while True:
            val = await queue.get()
            print("{} get a val:{}".format(id, val))
            await asyncio.sleep(1)


    async def producer(queue, id):
        for i in range(5):
            val = random.randint(1, 10)
            await queue.put(val)
            print("{} set a val:{}".format(id, val))
            await asyncio.sleep(1)


    async def main8():
        queue = asyncio.Queue()

        consumer_1 = asyncio.create_task(consumer(queue, "consumer_1"))
        consumer_2 = asyncio.create_task(consumer(queue, "consumer_2"))
        producer_1 = asyncio.create_task(producer(queue, "producer_1"))
        producer_2 = asyncio.create_task(producer(queue, "producer_2"))

        await asyncio.sleep(10)

        consumer_1.cancel()
        consumer_2.cancel()

        await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)


    start = time.perf_counter()
    asyncio.run(main8())
    end = time.perf_counter()
    print("8运行耗时{}秒".format(end - start))
