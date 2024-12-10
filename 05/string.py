# 字符串
if __name__ == "__main__":
    name = 'aaa'
    city = "bbb"
    text = """ccc"""
    print(name, city, text)

    # 转义符
    s = "a\nb\tc"
    print(s)
    print(len(s))

    # 支持索引及切片
    s = "lizhenzhen"
    print(s[1])
    print(s[2:6])

    # 改变字符串
    s = "hello"
    s = 'H' + s[1:]
    print(s)
    s = s.replace('H', 'h')
    print(s)

    # 字符串拼接，时间复杂度O(N)
    # s = ''
    # for n in range(0, 100000):
    #     s += str(n)
    # print(s)
    s1 = "li"
    s2 = "zhenzhen"
    s1 += s2
    print(s1)

    # join函数 时间复杂度O(N)
    # print(s1.join(s2))
    # l = []
    # for n in range(0, 100000):
    #     l.append(str(n))
    # l = ' '.join(l)
    # print(l)

    # 分隔符
    # split分割数据
    path = "hive://ads/training_table"
    namespace = path.split('//')[1].split('/')[0]
    table = path.split('//')[1].split('/')[1]
    print(namespace, table)

    # 内置函数
    # strip函数
    s = " my name is jason "
    print(s.strip())

    # 字符串格式化函数
    print("我的名字叫{},年龄{}".format("lzz", str(18)))

    # practice
    print("---------- practice ----------")

    # format
    personal_info = "my name is {}, I am {} years old".format("andy", str(18))
    print(personal_info)

    # split
    words = personal_info.split(" ")
    print(len(words))
    for word in words:
        print(word)


