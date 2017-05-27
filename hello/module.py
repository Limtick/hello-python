# -*- coding: utf-8 -*-

from drag_line import drag_line

from abs.my_abs import my_abs

drag_line('')
drag_line(123123123)
drag_line((1,2,3))
drag_line({'1':1})
drag_line([1,2,3,4])

print(my_abs(23))
print(my_abs(-2))
# print(my_abs('en'))

print('中文')
