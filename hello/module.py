# -*- coding: utf-8 -*-

from drag_line import drag_line

from abs.my_abs import my_abs
from abs.defs import fun1
from abs.defs import fun2

drag_line(
'''
定义默认参数要牢记一点：默认参数必须指向不变对象
必选参数、默认参数、可变参数、关键字参数和命名关键字参数
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
可变参数 *args  list tuple
关键字参数 **kw   dict
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict
'''
)

drag_line('')
drag_line(123123123)
drag_line((1,2,3))
drag_line({'1':1})
drag_line([1,2,3,4])

print(my_abs(23))
print(my_abs(-2))
# print(my_abs('en'))

print('中文')


drag_line('defs')
print(fun1(2))

print(fun1(5,3))
lists = [1,2,3]
print(fun2(*lists))
