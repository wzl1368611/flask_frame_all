#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index
from sqlalchemy import create_engine

Base = declarative_base()

# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))
    extra = Column(String(16))


def init_db():
    # 数据库连接相关
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
    # 创建表
    Base.metadata.create_all(engine)
def drop_db():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
    # 删除表
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    drop_db()
    init_db()
