# -*- coding: utf-8 -*-
r'''
    study


'''
# hello python

line = '----------华丽的分割线---------------\n'
def drag_line(str):
    if str:
        print('----------',str,'----------\n')
    else:
        print(line)

import sys

print ('Name is:',sys.argv[0])
print ('Path has:',sys.path)

def dump(module):
    print (module,'=>'),
    if module in sys.builtin_module_names:
        print ('内建模块')
    else :
        module = __import__(module)
        print (module.__file__)

dump('os')
dump('sys')
dump('string')
# dump('strop')
dump('zlib')

# sys 方法
# print ('methods is :', dir(sys))
drag_line('')
print('''sdsd
asdasd
asdasd
asdasd
asdasd
''')

print('I\'m ok!\n How are you?')
print(True)
print(False)

flag = 0>-1 or False
print(flag)

drag_line('2')

a= 'absc'
print('old a = ',a)
b = a
a = 'change'
print('''b = a
a = 'change'
''')
print('a has changed:',a)
print('b not change:',b)
drag_line('')

# 全部大写 常量  约定而已 gg
PI = 3.141592653
print(PI)

print(10/3)
print(10//3)

drag_line('文字编码')
print('中文')
love = '我爱你'
drag_line('中文不可以用ascii编码')
# print(love.encode('ascii'))
drag_line('utf-8 encode decode')
b_love = love.encode('utf-8')
print(love,'=> utf-8 encode =>',b_love)
love = b_love.decode('utf-8')
print(b_love,'b decode =>',love)

drag_line('')

print(ord('中'))
print(ord('文'))

print(chr(25991))
print(chr(20013))

x = b'adc'
print(x)

drag_line('字符串格式化 % ')

print('hello, %s' % ' world')
print('Hi,%s,you have %d fans!!!' % ('Limtick',1000000))
print('%2d-%02d' % (4, 2))
drag_line(
'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
)

s1 = 72
s2 = 85
percent = (s2 - s1) / s1
percent = percent * 100
print('72分提高到85分，提高了%.1f%s' % (percent,'%'))
drag_line('两个%转义为一个%')
print('72分提高到85分，提高了%.2f%%' % (percent))
drag_line('')
drag_line(
'''
Tips:
%d  -------  整数
%f  -------  浮点数
%s  -------  字符串
%x  -------  十六进制整数
example:
Hi,%s,you have %d fans!!!' % ('Limtick',1000000)
out:
Hi,Limtick,you have 1000000 fans!!!'
'''
)

drag_line('list')

members = ['jack','mark','小明']
print(members)
members_len = len(members)
print(members_len)
print(members[members_len-1])
print(members[1])
print(members[-1])

drag_line('')

member_copy = members
member_copy.append('new member')
members.insert(0,'haha')
member_copy.pop(1)
print(members)
print(member_copy)
drag_line('两个都会变化  证明赋值只是地址的映射')












exit()
name = input('Please enter name:')

print('Enter name is',name)

num1 = input('First Number:')
num2 = input('Second Number:')
print('result is:',num1*num2)
