#!/usr/lib/python3
import calendar
import time

print(time.time())

print(time.localtime())

print(time.asctime(time.localtime(time.time())))

tstr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(tstr)

print(time.strptime(tstr, "%Y-%m-%d %H:%M:%S"))

print(time.clock(), time.time())

time.sleep(1)

print(calendar.month(2018, 2))
print(time.localtime().tm_year)
print(calendar.isleap(time.localtime().tm_year))
