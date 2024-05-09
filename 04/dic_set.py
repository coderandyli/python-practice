# 集合与字典


# 通过商品ID获取价格
def find_product_price(products, product_id):
    for id, price in products:
        if (product_id == id):
            return price
    return None


products = [(1, 100),
            (2, 200),
            (3, 300),
            (4, 400)]

if __name__ == "__main__":
    # 初始化字典
    d1 = {'name': 'zhangsan', 'age': 18}
    d2 = dict({'name': 'zhangsan', 'age': 18})
    d3 = dict(name='zhangsan', age=18)
    print(d1 == d2 == d3)

    # 初始化集合
    s1 = {1, 2, 3}
    s2 = set([1, 2, 3])
    print(s1 == s2)

    # 混合类型
    s = {1, "hello", 5.0}
    print(s)

    # 元素访问
    d = {"name": "zym", "age": 20}
    print(d["name"])
    print(d.get("age"))
    print(d.get("locate", "null"))  # 值为空时，返回null

    s = {1, 2, 3}
    # print(s[1]) #本行出错

    # 判断是否在集合内
    s = {1, 2, 3}
    print(1 in s)
    print(4 in s)
    d = {"name": "zym", "age": 20}
    print("name" in d)
    print("location" in d)

    # 增删查改函数
    d = {"name": "zym", "age": 20}
    d["gender"] = "male"  # 增加元素
    d["dob"] = "1999-02-01"
    print(d)
    d["dob"] = "1998-01-01"  # 更新键值
    print(d)
    d.pop("dob")  # 删除键值
    print(d)

    s = {1, 2, 3}
    s.add(4)  # 增加元素
    print(s)
    s.remove(4)  # 删除元素
    print(s)

    # 字典排序
    d = {'b': 1, 'a': 2, 'c': 10}
    # 根据字典键的升序排序
    d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
    print(d_sorted_by_key)
    # 根据字典值的升序排序
    d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
    print(d_sorted_by_value)

    # 对集合排序
    s = [3, 4, 2, 1]
    s_sorted = sorted(s)
    print(s_sorted)

    # 获取产品价格
    price = find_product_price(products, 1)
    print(price)

