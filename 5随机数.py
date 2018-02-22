#!/usr/lib/python3
import random

# 从序列的元素中随机挑选一个元素
print(random.choice(range(10)))
# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
for i in range(10):
    print("randrange(0, 1000, 2) : ", random.randrange(0, 1000, 2))
for i in range(10):
    print("randrange(0, 1000, 3) : ", random.randrange(0, 1000, 3))
# 随机生成下一个实数，它在[0,1)范围内。
print(random.random())
# 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed(10)
print(random.random())
print(random.random())
# 将序列的所有元素随机排序
lst = [20, 16, 10, 5]
random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)
# 随机生成下一个实数，它在[x,y]范围内。
print(random.uniform(10, 20))
