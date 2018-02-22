#!/usr/lib/python3

strs = "abcd"
for it in strs:
    print(it)
else:
    print("over")

for index in range(len(strs)):
    print(index, strs[index])

print("over")

inp = input("\n\n请输入a/1或其它，按下 enter 键后退出。\n\n")
if inp == 'a':
    print("a")
elif inp == '1':
    print("1")
else:
    print("other")
