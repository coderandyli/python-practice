# 内存回收机制
'''
  - Python 中一切皆对象。因此，你所看到的一切变量，本质上都是对象的一个指针；
  - Python 使用标记清除（mark-sweep）算法和分代收集（generational），来启用针对循环引用的自动垃圾回收；
  - 垃圾回收是 Python 自带的机制，用于自动释放不会再用到的内存空间；
  - 引用计数是其中最简单的实现，不过切记，这只是充分非必要条件，因为循环引用需要通过不可达判定，来确定是否可以回收；
  - Python 的自动回收算法包括标记清除和分代收集，主要针对的是循环引用的垃圾收集；
  - 调试内存泄漏方面， objgraph 是很好的可视化分析工具。
'''
import os
import psutil
import sys


def show_memory_info(hint):
    pid = os.getpid()
    p  = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

# a是局部变量，对象指针无引用时，会被释放
# func()
# show_memory_info('finished')


def func2():
    show_memory_info('initial')
    global a
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

# a是全局变量，对象指针无引用时，会被释放
# func2()
# show_memory_info('finished')


print("--------- func3 ---------")
def func3():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')
    return a

# 生成的列表返回，然后在主程序中接收，那么引用依然存在
# a = func3()
# show_memory_info('finished')


# 引用计数
a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a)) # 查看一个变量的引用次数,getrefcount 本身也会引入一次计数。

def func4(a):
    # 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a))

func4(a)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(a))


# 手动释放内存
import gc

show_memory_info('initial')

a = [i for i in range(10000000)]

show_memory_info('after a created')

# 手动释放内存
del a
gc.collect()
show_memory_info('finish')

# 报错，NameError: name 'a' is not defined
# print(a)


# 循环引用，a与b循环引用导致引用计数不为0
def func5():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func5()
show_memory_info('finished')


# 循环引用手动释放
import gc
def func6():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func6()
gc.collect()
show_memory_info('finished')


# 调试内存泄漏
import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

# objgraph.show_refs([a])
objgraph.show_refs([a], filename = "objref.png")
objgraph.show_backrefs([a], filename = "backref.png" )

