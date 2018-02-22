#!/usr/lib/python3
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('连接地址：', addr)
    c.send(bytes("hello:" + str(addr[1]), "ascii"))
    print(c.recv(1024))
    c.close()
