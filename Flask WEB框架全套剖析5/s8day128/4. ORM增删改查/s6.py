

import models

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()

# 1. 在student表中插入数据
# obj = models.Student(username='梅凯',password='123',class_id=2)
# session.add(obj)
# session.commit()

# 2. 在学校表中找到梅凯
# obj = session.query(models.Student).filter(models.Student.username=='梅凯').first()
# print(obj)

# 3. 找到所有学生，打印学生信息(包含班级名称)
# objs = session.query(models.Student).all()
# for obj in objs:
#     cls_obj = session.query(models.Classes).filter(models.Classes.id==obj.class_id).first()
#     print(obj.id,obj.username,obj.class_id,cls_obj.name)

# objs = session.query(models.Student.id,models.Student.username,models.Classes.name).join(models.Classes,isouter=True).all()
# print(objs)

# objs = session.query(models.Student).all()
# for item in objs:
#     print(item.id,item.username,item.class_id,item.cls.name)

# 4. 全栈2期所有的学生
# obj = session.query(models.Classes).filter(models.Classes.name=='全栈2期099').first()
# student_list = obj.stus
# for item in student_list:
#     print(item.id,item.username)


session.close()
