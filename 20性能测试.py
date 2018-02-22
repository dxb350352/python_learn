import timeit

foooo = """
sum = []
for i in range(1000):
    sum.append(i)
"""

print(timeit.timeit(stmt="[i for i in range(1000)]", number=10000))
print(timeit.timeit(stmt=foooo, number=10000))

# 初始化类

y = """
simplejson.loads(x)
"""

print(timeit.timeit(stmt=y, setup="import simplejson; "
                                  "json={"
                                  "'id': 13423,"
                                  "'something': 'axiba',"
                                  "'extra_info': 'xiba',"
                                  "};"
                                  "x = simplejson.dumps(json)", number=10000))
