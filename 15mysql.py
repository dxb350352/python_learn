#!/usr/lib/python3
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect("192.168.130.201", "root", "123456.abcd", "gaxz")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Database version is %s add %s" % (data, "aa"))

# SQL 查询语句
sql = "SELECT * FROM statuses \
       WHERE id BETWEEN %d AND %d" % (10, 20)
print(sql)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # db.commit()
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as e:
    print(e.args)
    # db.rollback()

# 关闭数据库连接
db.close()
