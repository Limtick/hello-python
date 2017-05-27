# -*- coding: utf-8 -*-
# expected an indented block   缺少 pass
line = '----------华丽的分割线---------------\n'
def drag_line(a):
    # 非字符串转换
    if isinstance(a,(dict,list,tuple)):
        pass
        # print('hehe')
        # raise TypeError('bad operand type expect String')
    if not isinstance(a, (str,)):
        a = str(a)
        # raise TypeError('bad operand type expect String')
    if a:
        print('----------',a,'----------\n')
    else:
        print(line)
