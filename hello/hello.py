# -*- coding: utf-8 -*-
'''
    study
'''
# hello python

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

name = input('Please enter name:')
# exit()
print('Enter name is',name)

num1 = input('First Number:')
num2 = input('Second Number:')
print('result is:',num1*num2)
