import models

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()


# 单条增加
# obj = models.Classes(name='全栈1期')
# session.add(obj)
# session.commit()

# 多条增加
# objs = [
#     models.Classes(name='全栈2期'),
#     models.Classes(name='全栈3期'),
#     models.Classes(name='全栈4期')
# ]
# session.add_all(objs)
# session.commit()


session.close()
