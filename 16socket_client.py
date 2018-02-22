#!/usr/lib/python3
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口

s.connect((host, port))
print(s.recv(1024))
s.send(b"aaa")
s.close()
