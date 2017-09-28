#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
from io import StringIO
import json
import requests

r = requests.get(url='http://www.itwhy.org')    # 最基本的GET请求
print(r.status_code)    # 获取返回状态

r = requests.get('https://github.com/timeline.json')
print(r.encoding)
print(r.json())
# print(r.content)
print(r.text)

r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
# print(r.url)
# print(r.content)
