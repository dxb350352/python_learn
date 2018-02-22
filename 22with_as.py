#!/usr/bin/env python
'''
基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，
这个方法的返回值将被赋值给as后面的变量。
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
'''
import time


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("trace:", trace)
        print("type:", type)
        print("value:", value)

    def do_something(self, exp=True):
        if exp:
            1 / 0
        else:
            pass


# 只执行一次exit
with Sample() as sample:
    sample.do_something(False)
    sample.do_something(False)
    sample.do_something(False)
# 抛异常
with Sample() as sample:
    sample.do_something()
