#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import threading
import time

print("thread方式：")


def print_time(threadName, delay):
    count = 0
    while count < 2:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("t1", 1))
    _thread.start_new_thread(print_time, ("t2", 2))
except Exception as e:
    print(e.args)

print("threading方式：")

threadLock = threading.Lock()


class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter)
        # 释放锁，开启下一个线程
        threadLock.release()
        print("Exiting  " + self.name)


# 创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
