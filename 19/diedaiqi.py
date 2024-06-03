# 迭代器
import functools
import os
import time

import psutil

if __name__ == "__main__":
    # 判断一个对象是否可迭代
    def is_iterable(param):
        try:
            iter(param)
            return True
        except TypeError:
            return False


    params = [
        1234,
        '1234',
        [1, 2, 3, 4],
        set([1, 2, 3, 4]),
        {1: 1, 2: 2, 3: 3, 4: 4},
        (1, 2, 3, 4)
    ]
    for param in params:
        print("{} is iterable? {}".format(param, is_iterable(param)))


    # 生成器
    ## 显示当前python程序占用的内存大小
    def show_memory_info(hint):
        pid = os.getpid()
        p = psutil.Process(pid)

        info = p.memory_full_info()
        memory = info.uss / 1024. / 1024
        print("{} memory used: {}MB".format(hint, memory))


    def log_execution_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            start = time.perf_counter()
            res = func(*args, **kargs)
            end = time.perf_counter()
            print("函数{}运行耗时{}秒".format(func.__name__, end - start))
            return res

        return wrapper


    ## 迭代器版本
    @log_execution_time
    def test_iterator():
        print("初始化迭代器")
        list = [i for i in range(10000000)]
        show_memory_info("初始化迭代器后")
        print(sum(list))
        show_memory_info("调用sum后")


    ## 生成器版本
    @log_execution_time
    def test_generator():
        show_memory_info("初始化生成器")
        list2 = (i for i in range(10000000))
        show_memory_info("初始化生成器以后")
        print(sum(list2))
        show_memory_info("调用sum以后")


    test_iterator()  # 386.0MB
    print()
    test_generator()  # 7.359375MB


    # 生成器的使用
    '''
    用例：数学中有一个恒等式，(1 + 2 + 3 + ... + n)^2 = 1^3 + 2^3 + 3^3 + ... + n^3。
    yield: 创建一个生成器
    '''
    def generator(k):
        i = 1
        while True:
            yield i ** k  ## i^k
            i += 1


    gen_1 = generator(1)
    gen_3 = generator(3)


    def get_sum(n):
        sum_1, sum_3 = 0, 0
        for i in range(n):
            next_1 = next(gen_1)  # 1, 2, 3, 4
            next_3 = next(gen_3)  # 1^3), 2^3, 3^3, 4^3
            print("next_1={}, next_3={}".format(next_1, next_3))
            sum_1 += next_1
            sum_3 += next_3
        print(sum_1 * sum_1, sum_3)


    get_sum(8)


    # 生成器的另一个例子，找指定元素在列表中的位置
    def index_generator(L, target):
        for i, num in enumerate(L):
            if num == target:
                yield i


    print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))


    # 给定两个有序序列，判断第一个是不是第二个的子序列
    def is_subsequence(a, b):
        b = iter(b)
        return all(i in b for i in a)


    print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
    print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))


    # 思考题 有限元素生成器无限迭代
    gen = (i for i in range(5))
    for i in range(10):
        print(next(gen))
