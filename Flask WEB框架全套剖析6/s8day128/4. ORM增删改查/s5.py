import models

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()

# select id,name from classes
# session.query(models.Classes).all()
# select id,name as nn from classes
# 1
# result = session.query(models.Classes.id,models.Classes.name.label('xx')).all()
# for item in result:
#     # print(item[0],item[1])
#     print(item.id,item.xx)
# 2. filter/filter_by
# r3 = session.query(models.Classes).filter(models.Classes.name == "alex").all()
# r4 = session.query(models.Classes).filter_by(name='alex').all()

# 3. 子查询
# result = session.query(models.Classes).from_statement(text("SELECT * FROM classes where name=:name")).params(name='ed').all()
# result = session.query(models.Classes).from_statement(text("SELECT * FROM classes where name=:name")).params(name='ed')
# # 子查询
# ret = session.query(models.Classes).filter(models.Classes.id.in_(session.query(models.Classes.id).filter_by(name='eric'))).all()
# # 关联子查询
# subqry = session.query(func.count(Server.id).label("sid")).filter(Server.id == Group.id).correlate(Group).as_scalar()
# result = session.query(Group.name, subqry)



session.close()
