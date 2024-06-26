# coding:utf-8
# 第15课 Python对象比较、拷贝
"""
	值传递:通常就是拷贝参数的值，然后传递给函数里的新变量。这样，原变量和新变量之间互相独立，互不影响
	引用传递：通常是指把参数的引用传给新的变量，这样，原变量和新变量就会指向同一块内存地址，如果改变了其中任何一个变量的值，那么另外一个变量也会相应地随之改变。

	*** Python 的参数传递是赋值传递 （pass by assignment），或者叫作对象的引用传递（pass by object reference）。Python 里所有的数据类型都是对象，所以参数传递时，只是让新变量与原变量指向相同的对象而已，并不存在值传递或是引用传递一说 ***
"""

import copy


if __name__ == "__main__":
	a = 2
	b = 2
	print(a == b)
	print(a is b)
	print("id(a) = {}".format(id(a)))
	print("id(b) = {}".format(id(b)))
	# 以上只对-5至256的值有效 （python3.9版本已上，1000000000也有效）
	a = 1000000000
	b = 1000000000
	print(a == b)
	print(a is b) # python3.9版本以上，为true
	print("id(a) = {}".format(id(a)))
	print("id(b) = {}".format(id(b)))
	
	# 对于不可变变量
	t1 = (1, 2, [3, 4])
	t2 = (1, 2, [3, 4])
	print(t1 == t2)
	print(id(t1), id(t2))
	t1[-1].append(5)
	print(t1 == t2) # false
	print(id(t1), id(t2))

	# 浅拷贝
	l1 = [1, 2, 3]
	l2 = list(l1)
	print(l1 == l2)
	print(l1 is l2)
	s1 = set([1, 2, 3])
	s2 = set(s1)
	print(s1, s2)
	print(s1 == s2)
	print(s1 is s2)
	# 通过切片操作
	l1 = [1, 2, 3]
	l2 = l1[:]
	print(l1 == l2)
	print(l1 is l2)
	# 使用copy函数
	l2 = copy.copy(l1)
	print(l1 == l2)
	print(l1 is l2)
	# 元组的不同，返回一个指向元组的引用
	t1 = (1,2,3)
	t2 = tuple(t1)
	print(t1 == t2)
	print(t1 is t2)

	# 浅拷贝的副作用
	l1 = [[1, 2], (30, 40)]
	l2 = list(l1)
	l1.append(100)
	l1[0].append(3)
	print(l1)
	print(l2)
	l1[1] += (50, 60)
	print(l1)
	print(l2)

	# 深拷贝
	l1 = [[1, 2], (30, 40)]
	l2 = copy.deepcopy(l1)
	l1.append(100)
	l1[0].append(3)
	print(l1, l2)
	# 陷入无限循环的深拷贝
	x = [1]
	x.append(x)
	print(x)
	y = copy.deepcopy(x)
	print(y)
	# 思考题
	# print(x == y) #报错
	print(x is y)