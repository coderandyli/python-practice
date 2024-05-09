
if __name__ == "__main__":

    l = [1, 2, 3, 4, 'five', 6] # 列表
    tuple = (1, 2, 3, 4, 'five', 6) # 元组
    print(l)
    print(tuple)

    # 元素替换
    l[3] = 40 # 列表，元素替换
    print(l)
    # tuple[3] = 40  # 元组，不支持元素替换

    # 添加元素
    l.append(7)
    print(l)
    new_tuple = tuple + (7,)

    # 切片操作
    print(l[4:6])
    print(tuple[4:6])

    # 嵌套
    l = [[1,'a'], [2,'b']]
    tuple = ([1,'a'],[2,'b'])
    print(l)
    print(tuple)

    # 内置函数
    l = [1, 2, 3, 4, 5, 6, 3]
    print(l.count(3))
    print(l.index(4))
    l.reverse()
    print(l)
    l.sort()
    print(l)
    l.reverse()
    print(l)
    l.remove(3)
    print(l)
    l.remove(4)  # ==4的元素
    print(l)

    # 元祖转换为列表
    l = [1, 2, 3, 4, 5, 6]
    tuple = (1,3, 2,  4, 5, 6)
    print(list(reversed(tuple))) # 转为列表
    print(sorted(tuple))

