#!D:\ProgramFiles\Anaconda3\python.exe
import keyword

str = '''
hello
world
fds
'''
print("hello world", str)
print("你好，世界")
print(r'\n')
print(R'\n')

print("python保留字:", keyword.kwlist)

# end
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
