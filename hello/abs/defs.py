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
