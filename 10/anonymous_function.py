# 匿名函数
import operator

if __name__ == "__main__":
    # lamda 表达式
    square = lambda x: x**2
    print(square(3))

    # 列表内部使用
    l1 = [x for x in range(10)]
    l2 = [(lambda x:x**2) (x) for x in range(10)]
    print(l1)
    print(l2)

    # 用作函数参数
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1]) #正序
    print(l)
    l.sort(key=lambda x: x[1], reverse = True) #倒叙
    print(l)

    # map函数
    l = [1, 3, 5, 6, 8]
    new_list = list(map(lambda x: x ** 2, l))
    print(new_list)

    l = [1, 3, 5, 7, 9]
    new_list = list(filter(lambda x: x != 3, l)) # 过滤3
    print(new_list)

    # reduce函数 计算阶乘
    from functools import reduce
    l = [2, 3, 4]
    product = reduce(lambda x, y: x * y, l)
    print(product)

    # 函数式编程，将列表元素加倍
    def mutiply_2_pure(l):
        new_list = []
        for item in l:
            new_list.append(item * 2)
        return new_list

    print(mutiply_2_pure([1, 2, 3, 4]))

    # 思考题
    d = {"mike": 10, "lucy": 2, "ben": 30}
    print(d.items())
    sort_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    print(sort_d)