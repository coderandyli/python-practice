from concurrent.futures import CancelledError, BrokenExecutor

# coding:utf-8
# 第21课 Python并发编程之futures


import requests
import time
import concurrent.futures

from aiohttp import TooManyRedirects
from requests import HTTPError, Timeout


# 单线程版下载
def download_one(url):
    resp = requests.get(url)
    print("read {} from {}".format(len(resp.content), url))


def download_all(sites):
    for site in sites:
        download_one(site)


# 多线程版下载
def download_all_futures(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


# 并行版
def download_all_futures_bx(sites):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


# 另一种写法的并行版本
def download_all_futures_bx2(sites):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()


if __name__ == "__main__":
    sites = [
        'https://www.e-ports.com.cn/zh/shipping/news/e61df60133b94dba9e2b852671be2703',
        'https://www.e-ports.com.cn/zh/shipping/news/dc8aa8dca9a5446caf76c15c87b00554',
        'https://www.e-ports.com.cn/zh/shipping/news/7f5b8338ecc0402681f559be7b055238',
        'https://www.e-ports.com.cn/zh/shipping/news/b753bb43b3a0434797c8562c5b3cf7bc',
        'https://www.e-ports.com.cn/zh/shipping/news/4149c6fda8564818b0a8791deb741c06',
        'https://www.e-ports.com.cn/zh/shipping/news/5ae1ae6c339b4ac2958928abd19d4763',
        'https://www.e-ports.com.cn/zh/shipping/news/020a90cfb2924919b78f659ddf3bcd60',
        'https://www.e-ports.com.cn/zh/shipping/news/890c7f9ead1b4c93a3f7f9ec0e11f779'
    ]
    try:
        start_time = time.perf_counter()
        download_all(sites)
        end_time = time.perf_counter()
        print("单线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures(sites)
        end_time = time.perf_counter()
        print("多线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures_bx(sites)
        end_time = time.perf_counter()
        print("并行版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))

        start_time = time.perf_counter()
        download_all_futures_bx2(sites)
        end_time = time.perf_counter()
        print("另一个并行版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))
    # 处理requests异常
    except ConnectionError as err:
        print(err)
    except HTTPError as err:
        print(err)
    except Timeout as err:
        print(err)
    # 处理futures异常
    except TooManyRedirects as err:
        print(err)
    except CancelledError as err:
        print(err)
    except TimeoutError as err:
        print(err)
    except BrokenExecutor as err:
        print(err)
    except:
        print("发生错误")
