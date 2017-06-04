#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from drag_line import drag_line
r'''
    列表生成表达式
'''
a = [x * x for x in range(1, 11)]

print(a)

# 判断
b = [x * x for x in range(1, 11) if x % 2 == 0]

print(b)
# 双层
c = [m + n for m in 'ABC' for n in 'XYZ']

print(c)

d = {'x': 'A', 'y': 'B', 'z': 'C'}

e = [k + '=' + v for k, v in d.items()]
print(e)

L = ['Hello', 'World', 'IBM', 'Apple', 123, 2323]

l = [s.lower() for s in L if isinstance(s, str)]
print(l)


r'''
    一边循环一边计算的机制，称为生成器：generator
'''
drag_line('第一种方法  使用()代替[]')
g = (x * x for x in range(10))
print(g)
# next(g)  调用  可惜实际基本不会用到
# 因为generator也可以迭代
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
for x in g:
    print(x)

drag_line('斐波拉契数列（Fibonacci）')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # t = (a,a+b)  tuple
        # a = t[0]
        # b = t[1]
        a, b = b, a + b
        n += 1
    return 'finish'


print(fib(6))
drag_line(
    '''
第二种方法
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
'''
)


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # t = (a,a+b)  tuple
        # a = t[0]
        # b = t[1]
        a, b = b, a + b
        n += 1
    return 'finish'


example = fib_generator(6)
print(example)  # generator
for x in example:
    print(x)
drag_line(
'''
for循环调用generator时，拿不到generator的return语句的返回值
必须捕获StopIteration错误，返回值包含在StopIteration的value中
''')
g = fib_generator(6)
while True:
    try:
        n = next(g)
        print(n)
    except StopIteration as e:
        print(e.value)
        break

def triangles(num):
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
        if len(a) > num:
            break
t = triangles(10)
for i in t:
    print(i)
