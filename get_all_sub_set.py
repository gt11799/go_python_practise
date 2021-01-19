# coding: utf-8
# 求字符串的子集
# 123 -> 1，2，3，12，13，23，123，子集的个数，字符串里没有重复的字符
# 12345 1 23 13 34 135
# 1 2 3 4 5 
# 12 23 25
# 12345 13452


# 使用了python的库，比较投机
def get_all_string_simple(string):
    from itertools import combinations
    l = list(string)
    result = []
    for i in range(1, len(l) + 1):
        for item in combinations(l, i):
            result.append(",".join(item))
    return result


# 参照combinations的方式，其实就是按照不同的数量，去逐渐遍历出所有的组合，因此只要实现combitions即可
import copy
def combine(l, n):
    result = []
    one = [0] * n
    def next_c(li=0, ni=0):
        if ni == n:
            result.append(copy.copy(one))
            return
        for lj in range(li, len(l)):
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return result


def get_all_sub_string(string):
    l = list(string)
    result = []
    for i in range(1, len(l) + 1):
        for item in combine(l, i):
            result.append(",".join(item))
    return result


result = get_all_sub_string("12345")
print len(result), result
r = get_all_string_simple("12345")
print len(r), r
