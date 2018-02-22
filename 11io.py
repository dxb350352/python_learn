#!/usr/lib/python3
# -*- coding: UTF-8 -*-

import os

import time

try:
    # f = open("D:/test.txt", os.O_RDWR)
    f = open("D:/test.txt", "a+")
    print(f.readlines())
    f.write(str(time.time()) + "\n")
    # raise Exception("Invalid level!", 1)
except IOError as e:
    print(e.strerror, "....")
except Exception as e:
    print(e.args)
else:  # 无异常才执行
    f.close()
finally:
    print("over")

f = os.open("D:/test.txt", os.O_RDWR)
print(os.read(f, 10))
os.close(f)

f = open("D:/test.txt", "r+")
while True:
    try:
        print(next(f), end="")
    except StopIteration:
        break
f.close()
