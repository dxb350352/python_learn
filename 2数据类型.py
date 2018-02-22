#!usr/lib/python3

number = 1
print(number)
del number
# print(var1)#要报错了

str1 = 'Hello World!'
print(str1 * 2)  # 输出字符串两次
print(str1[-1])

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表
print(list[-1])

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

numstr = "1.1"
print(str(float(numstr)))
print(eval(repr(tinydict)))
print(ord(chr(65)))
