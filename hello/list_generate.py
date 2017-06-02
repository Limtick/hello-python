#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from drag_line import drag_line

a = [x * x for x in range(1, 11)]

print(a)

# 判断
b = [x * x for x in range(1, 11) if x % 2 == 0]

print(b)
# 双层
c = [m + n for m in 'ABC' for n in 'XYZ']

print(c)

d = {'x': 'A', 'y': 'B', 'z': 'C' }

e = [k + '=' + v for k,v in d.items()]
print(e)

L = ['Hello', 'World', 'IBM', 'Apple',123,2323]

l = [s.lower() for s in L if isinstance(s, str)]
print(l)
