#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_obj = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_obj)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_obj)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# 文件
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(json_obj, f)

# 读取数据
with open('data.json', 'r') as f:
    print(json.load(f))
