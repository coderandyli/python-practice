# 单元测试

import unittest
from unittest.mock import MagicMock

import MagicMock


# 将要测试的排序函数
def sort(arr):
	l = len(arr)
	for i in range(0, l):
		for j in range(i + 1, l):
			if arr[i] >= arr[j]:
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp

# 单元测试
class TestSort(unittest.TestCase):
    # 以test开头的函数会被测试
    def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        self.assertEqual(arr, [1, 3, 4, 5, 6])


# mock
class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called) #验证m2被call过
        a.m3.assert_called_with("custom_val") #验证m3被指定参数call过

def side_effect(arg):
	if arg < 0:
		return 1
	else:
		return 2

if __name__ == '__main__':
    unittest.main()

    # Mock Side Effect，这个概念很好理解，就是 mock 的函数，属性是可以根据不同的输入，返回不同的数值，而不只是一个 return_value。
    mock = MagicMock()
    mock.side_effect = side_effect
    print(mock(1))
    print(mock(-2))