#  装饰器
import functools
import time
from functools import lru_cache

if __name__ == "__main__":
    # 函数作为变量
    def func(message):
        print("收到一个消息：{}".format(message))
    send_message = func
    send_message("你好")

    # 函数作为变量
    def root_call(fun, message):
        print(fun(message))
    root_call(func, "函数参数")

    # 函数嵌套
    def fund(message):
        def get_message(msg):
            print("收到一个消息：{}".format(msg))
        return get_message(message)
    fund("函数嵌套")

    # 闭包: 函数的返回值也可以是函数对象
    def func_closure():
        def get_msg(msg):
            print("收到一个消息: {}".format(msg))
        return get_msg
    send_message = func_closure()
    send_message("闭包")

    # 简单的装饰器
    print("------------ 简单的装饰器 ------------")
    def my_decorator(func):
        def wrapper():
            print("装饰器")
            func()
        return wrapper

    def greet():
        print("你好")

    greet = my_decorator(greet)
    greet()

    # 原函数还是原函数吗？
    print(greet.__name__)
    print(help(greet))

    print("------------ 使用functools.wrap ------------")
    def my_decorator2(func):
        @functools.wraps(func) # 帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）, 不加该注释元信息将不再是原函数
        def wrapper(*args, **kwargs): # *args, **kwargs 表示接受任意数量和类型的参数
            print("functools的装饰器")
            func(*args, **kwargs)

        return wrapper

    @my_decorator2
    def greet2(message):
        print(message)

    greet2("functools")
    # print(greet2.__name__)

    print("------------ 类装饰器 ------------")
    class Count():
        def __init__(self, func):
            self.func = func
            self.num_calls = 0

        def __call__(self, *args, **kwargs):
            self.num_calls += 1
            print("num of call is {}".format(self.num_calls))
            return self.func(*args, **kwargs)

    @Count
    def example():
        print("类装饰器")

    example()
    example()

    print("------------ 装饰器嵌套 ------------")
    def my_decorator_a(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("functools的装饰器a")
            func(*args, **kwargs)

        return wrapper

    def my_decorator_b(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("functools的装饰器b")
            func(*args, **kwargs)

        return wrapper

    @my_decorator_a
    @my_decorator_b
    def greet3(message):
        print(message)

    greet3("functools")
    print(greet3.__name__)

    print("------------ 应用举例-给函数加上计时功能 ------------")
    def log_execution_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            start = time.perf_counter()
            res = func(*args, **kargs)
            end = time.perf_counter()
            print("函数{}运行耗时{}秒".format(func.__name__, end - start))
            return res
        return wrapper

    @log_execution_time
    def add(n):
        s = 0
        for i in range(n):
            s += i
        return s

    res = add(10000)
    print(res)


    @log_execution_time
    def multiply(n):
        s = 1
        for i in range(n):
            s = s * (i + 1)
        return s

    res = multiply(10000)
    print(res)
