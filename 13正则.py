#!/usr/lib/python3

import re

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs"
pattern = re.compile(r"(.*) are", re.M | re.I)
matchObj = pattern.match(line)
# matchObj = re.search(r"are (.*?) .*", line, re.M | re.I)
if matchObj:
    print(matchObj.group())
    for g in matchObj.groups():
        print(g)

phone = "2004-959-559 # 这是一个国外电话号码"
print(re.sub(r"#.*", "\b0", phone))
print(re.sub(r"\D", "", phone))
print(re.sub(r"\d+", lambda mted: str(int(mted.group()) * 2), phone))
# 分组，除了原有的编号外再指定一个额外的别名
print(re.sub(r"(?P<value>\d+)", lambda mted: str(int(mted.group('value')) * 2), phone))

print(re.split(r'\W+', "hello ?走你 ,我 re"))
