#!/usr/lib/python3

list = [1, 2, 3, 3]  # 空列表
list.reverse()
print(list)
list.sort()
print(list)
list.append('Google')  # 使用 append() 添加元素
print(list)
del list[0]
list.remove(2)
print(list)
print(len(list))
print(list.count(3))
