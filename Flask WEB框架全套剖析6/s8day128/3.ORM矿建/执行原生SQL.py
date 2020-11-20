#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
cur = engine.execute('select * from users')
result = cur.fetchall()
print(result)

