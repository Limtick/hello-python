#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fun1(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def fun2(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
    # 命名关键字参数 特殊分隔符*，*后面的参数被视为命名关键字参数   本例为city job
    # 有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了   name, age, *args, city, job
def person(name, age, *, city, job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
