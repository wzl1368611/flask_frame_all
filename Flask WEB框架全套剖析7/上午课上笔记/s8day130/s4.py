import models
from threading import Thread
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8",pool_size=2,max_overflow=0)
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()

def task():

    data = session.query(models.Classes).all()
    print(data)

    session.close()

for i in range(10):
    t = Thread(target=task)
    t.start()
