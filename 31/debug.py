# 第31课 pdb与cProfile
'''
    - pdb debug：https://docs.python.org/3/library/pdb.html#module-pdb
    - cProfile性能分析：https://docs.python.org/3.7/library/profile.html
'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res

# print(fib_seq(30))

import cProfile
# def fib(n)
# def fib_seq(n):
cProfile.run('fib_seq(30)')

# if __name__ == '__main__':
#     a = 1
#     b = 2
#     import pdb
#
#     pdb.set_trace()
#     c = 3
#     print(a + b + c)