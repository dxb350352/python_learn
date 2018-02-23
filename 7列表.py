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

# 列表推导式(集合也可)
print("列表推导式")


def dosomething(x, y, z):
    return (x + y) * z


vec = [1, 2, 3]
vec2 = [4, 5, 6]
print("[1 + it for it in vec if it % 2 == 1]->", [1 + it for it in vec if it % 2 == 1])
print("[(1 + it) for it in range(1, 4)]->", [(1 + it) for it in range(1, 4)])
print("[[1 + it] for it in vec]->", [[1 + it] for it in vec])
print("[[1 + it, it ** 2] for it in vec]->", [[1 + it, it ** 2] for it in vec])
print("[dosomething(it, 1, 2) for it in vec]->", [dosomething(it, 1, 2) for it in vec])
print("[x + y for x in vec for y in vec2]->", [x + y for x in vec for y in vec2])
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print("[[row[i] for row in matrix] for i in range(4)]->", [[row[i] for row in matrix] for i in range(4)])
print("[row[i] for row in matrix for i in range(4)]->", [row[i] for row in matrix for i in range(4)])

# 集合set
print("set")
Set = {1, 2, 3, 3, 2, 1}
print(Set)
empty = set()
empty.add(1)
print(empty)
a = set('abc')
print("a->", sorted(a))
b = set('bcd')
print("b->", b)
print("a - b->", a - b)
print("a | b->", a | b)
print("a & b->", a & b)
print("a ^ b->", a ^ b)
