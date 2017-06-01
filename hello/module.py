# -*- coding: utf-8 -*-

from drag_line import drag_line

from abs.my_abs import my_abs
from abs.defs import fun1
from abs.defs import fun2
from abs.defs import f1
from abs.defs import f2

drag_line(
'''
定义默认参数要牢记一点：默认参数必须指向不变对象
必选参数、默认参数、可变参数、关键字参数和命名关键字参数
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
可变参数 *args  list tuple
关键字参数 **kw   dict
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
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
drag_line('')

f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

drag_line('')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

drag_line('递归')

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
# stackoverflow
# print(factorial(1000))

# 尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
# 并没有什么卵用
# print(fact(1000))

# 汉诺塔递归
i = 0
def move(n, a, buffer, c):
    global i
    if(n == 1):
        print(a,"->",c)
        i += 1
        return
    # a柱的上面的n-1个，通过c按照从小到大的规则先移动到缓冲区buffer
    move(n-1, a, c, buffer)
    # a柱上的一个盘子移动到c
    move(1, a, buffer, c)
    # n-1个通过a当缓冲区移动到c
    move(n-1, buffer, a, c)
move(5, "a", "b", "c")
print(i)
