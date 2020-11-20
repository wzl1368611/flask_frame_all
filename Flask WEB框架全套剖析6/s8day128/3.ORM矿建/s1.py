import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()



obj1 = models.Users(name="alex", extra='sb')
obj2 = models.Users(name="alex", extra='db')
session.add(obj1)
session.add(obj2)


session.commit()