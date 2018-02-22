#!/usr/lib/python3

a = [1, 2, 3]
print(a)
a = "d"
print(a)


def go(a, b=1):
    print(a, b)


go(a=2)


def gogo(a, *xx, **yy):
    print(a)
    for t in xx:
        print(t, "xx")
    for k, v in yy.items():
        print(k, v, "yy")


gogo(1, 2, 3, 4, aa=1, bb=2)

sum = lambda a1, a2: a1 + a2
print(sum(1, 2))

print(dir())
