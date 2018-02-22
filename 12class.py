#!/usr/lib/python3


class User:
    """类的文档字符串"""
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 1

    @staticmethod
    def print(*values):
        print(*values)

    @classmethod
    def print2(cls, *values):
        print(*values)

    def display(self):
        self.print(self.__dict__, User.count)


User.print("1", 2)
User.print2("1", 2)
User("name", 1).display()
User("name", 2).display()
user = User("name", 3)
user.salary = 1000
print(user.salary)
del user.salary

setattr(user, "name", "new")
print(getattr(user, "name"))

print(user.__dict__)
print(vars(user))
print(User.__dict__)
print(User.__doc__)
print(User.__module__)
print(User.__name__)
print(User.__bases__)


# 继承
class Child(User):
    def __init__(self):
        self.__init_subclass__()


child = Child()
print(issubclass(User.__class__, Child.__class__))
print(isinstance(child, Child))


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
