#!/usr/bin/python3
from pylint.checkers.spelling import maketrans

strs = "hello wORLD"
print(strs.capitalize())
print(strs.center(20, '*'))
print(strs.isalnum())
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置


class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

print("123.123".isdecimal())
print("123.123".isdigit())
print("123.123".isnumeric())
print("四".isdecimal())
print("IV".isdigit())
print("四".isnumeric())

print("-".join(["a", "b", "c"]))
print(strs.ljust(20, '0'))

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab))

print(strs.partition("o w"))
print(strs.swapcase())
