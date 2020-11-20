#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Index,DateTime,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import datetime
Base = declarative_base()

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False,unique=True)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False,index=True)
    password = Column(String(64), nullable=False)
    ctime = Column(DateTime,default=datetime.datetime.now)
    class_id = Column(Integer, ForeignKey("classes.id"))

    cls = relationship("Classes", backref='stus')


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')

class Student2Hobby(Base):
    __tablename__ = 'student2hobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    hobby_id = Column(Integer, ForeignKey('hobby.id'))

    __table_args__ = (
        UniqueConstraint('student_id', 'hobby_id', name='uix_student_id_hobby_id'),
        # Index('ix_id_name', 'name', 'extra'),
    )

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
    # drop_db()
    init_db()