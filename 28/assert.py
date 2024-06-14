# 28 | 如何合理利用assert？
'''
    - 这里的__debug__是一个常数。如果 Python 程序执行时附带了-O这个选项，比如Python test.py -O，那么程序中所有的 assert 语句都会失效，常数__debug__便为 False；反之__debug__则为 True。
    - assert 在程序中的作用，是对代码做一些 internal 的 self-check。使用 assert，就表示你很确定。这个条件一定会发生或者一定不会发生。
    - assert 的加入，可以有效预防 bug 的发生，提高程序的健壮性。
    - assert是可以通过加入-O这个选项让 assert 失效的，因此assert 并不适用run-time error的检查，运行时异常需要使用异常处理（raise Exception('xxx')）
'''

# 抛出异常
# assert 1 == 2, 'This should fail'

#
def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price

# print(apply_discount(100, 0.2))
# print(apply_discount(100, 1.1))


def calculate_average_price(total_sales, num_sales):
    assert num_sales > 0, 'number of sales should be greater than 0'
    return total_sales / num_sales

# print(calculate_average_price(10, -1))

# 入参必须是list
def func(input):
    assert isinstance(input, list), 'input must be type of list'
    # 下面的操作都是基于前提：input必须是list
    if len(input) == 1:
        ...
    elif len(input) == 2:
        ...
    else:
        ...

func("this is a error arguments")