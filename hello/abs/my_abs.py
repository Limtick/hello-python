# -*- coding: utf-8 -*-
#  pep8 -> pip install --upgrade autopep8


def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type expect Number')
    if num > 0:
        return num
    else:
        return -num
