#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 不推荐这种引入
import sys
sys.path.append("..")
from drag_line import drag_line

drag_line('')
r'''
    切片
'''
a = list(range(100))

# 前包后不包
# 首位为0可以省略
print(a[0:5])
print(a[:5])
print(a[1:5])

drag_line('')

print(a[-10:-5])
# 5-20   每2个取一个
print(a[5:20:2])
# 所有  每10个一个
print(a[::10])
# 复制
print(a[:])
drag_line('')

b = 'abcdefg'
print(b[1:3])




drag_line('ddd')
r'''
    迭代
'''

# 判断是否可以迭代
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

drag_line('迭代')
list = list(range(10))
for key in list:
    print(key)

array = [1, 2, 5, 3, 6, 8, 4]
print(sorted(array))
drag_line('---')
r'''
dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
'''
d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)

for k, v in d.items():
    print(k,'is',v)

drag_line('')
# enumerate吧list转为键值对
for i, value in enumerate(['A', 'B', 'C']):
    print(i,'---',value)
drag_line('多个参数')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
