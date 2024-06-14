# 定一个非递减整数数组，和一个 target，要求你找到数组中最小的一个数 x，可以满足 x*x > target。一旦不存在，则返回 -1。
def solve(arr, target):
    l, r = 0, len(arr) - 1
    ret = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] * arr[m] > target:
            ret = m
            r = m - 1
        else:
            l = m + 1
    if ret == -1:
        return -1
    else:
        return arr[ret]


print(solve([1, 2, 3, 4, 5, 6], 8))
print(solve([1, 2, 3, 4, 5, 6], 9))
print(solve([1, 2, 3, 4, 5, 6], 0))
print(solve([1, 2, 3, 4, 5, 6], 40))
