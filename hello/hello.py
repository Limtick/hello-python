# -*- coding: utf-8 -*-
r'''
    study
    数据类型
    str
        Tips:
        %d  -------  整数
        %f  -------  浮点数
        %s  -------  字符串
        %x  -------  十六进制整数
        example:
        Hi,%s,you have %d fans!!!' % ('Limtick',1000000)
        out:
        Hi,Limtick,you have 1000000 fans!!!'
        '72分提高到85分，提高了%.1f%s' % (percent,'%')
        drag_line('两个%转义为一个%')
        '72分提高到85分，提高了%.2f%%' % (percent)
        如果字符串里面有很多字符都需要转义，就需要加很多\，
        为了简化，Python还允许用r''表示''内部的字符串默认不转义
        单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
        对bytes类型的数据用带b前缀的单引号或双引号
        encode()  decode()  转换为bytes
    int
    float
    bool
        True  False  and or not
    None
    list [1,2,3,4,5]  len()  list(index)
    tuple (1,2,3,4,5)  元组,不可修改(指向,指向中的list仍然可以修改)
        list[index]   取index位置   不能超过len
        list[-1] list[-2]  -1取最后一个  -2前推
        append('dd') 追加到末尾
        pop(index)  删除index位置的项
        insert(index,'dd')  指定位置插入
        tuple  固定  但是里面的list数组可以被改变  不变的是指向
        range生成一个序列，list方法可以转换为数组  for循环累加
    dict {'name':'jack','type':'python'}

    set  set([2,4,5,6])
        set
        add(key) 添加
        remove(key) 删除
        help(method)  查看帮助

'''
# hello python



import sys
from drag_line import drag_line

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
'72分提高到85分，提高了%.1f%s' % (percent,'%')
drag_line('两个%转义为一个%')
'72分提高到85分，提高了%.2f%%' % (percent)
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
member_copy.insert(1,'jack')
member_copy[4] = 'update'
print(members)
print(member_copy)
LIST = (1,2)

drag_line('两个都会变化  证明赋值只是地址的映射')
print(LIST)
drag_line(
'''
list[index]   取index位置   不能超过len
list[-1] list[-2]  -1取最后一个  -2前推
append('dd') 追加到末尾
pop(index)  删除index位置的项
insert(index,'dd')  指定位置插入
tuple  固定  但是里面的list数组可以被改变  不变的是指向
range生成一个序列，list方法可以转换为数组  for循环累加
''')

nums = range(101)
nums = list(nums)
sum = 0
for n in nums:
    sum = sum + n
print(nums)
print(sum)

drag_line('dict')

obj = {'name':'jack','age':18}
print(obj)
print(obj['name'])
if 'type' in obj:
    print(obj['type'])
else:
    print('type不存在')
drag_line(
'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
'''
)

drag_line('set')

a = set([1,2,34,5])
b = set([1,3,4,6,5])
a.add('5')
b.remove(1)
print(a)
print(b)
drag_line(
'''
< <= 表示 子集，> >=表示超集
| 表示联合 & 表示交集 - 表示差集 ^ 差分集
'''
)
print(a&b)
print(a|b)
print(a-b)
print(a^b)

print(set((1,2,3)))

drag_line(
'''
set
add(key) 添加
remove(key) 删除
help(method)  查看帮助
'''
)

print(help(abs))









exit()
name = input('Please enter name:')

print('Enter name is',name)

num1 = input('First Number:')
num2 = input('Second Number:')
num1 = int(num1)
num2 = int(num2)
print('result is:',num1*num2)

drag_line('int方法将字符串数字转换为Number数字')
