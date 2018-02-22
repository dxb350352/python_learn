#!/usr/lib/python3

a, b = 2, 3
print(a ** b)  # 幂
print(b // a)  # 取整除 - 返回商的整数部分

print(a and b)
print(a or b)
print(not b)

list = [1, 2, 4]
print(a in list)
print(b not in list)
print("1" in "321")

# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
print(id(a), id(b))
print(a is a)
print(a is not b)

