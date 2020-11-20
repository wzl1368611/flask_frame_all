import models
from threading import Thread
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8",pool_size=2,max_overflow=0)
XXXXXX = sessionmaker(bind=engine)
# 原来：session=XXXXXX()

"""
session = scoped_session对象 {
    session_factory = XXXXXX,
    registry = ThreadLocalRegistry{
        createfunc=XXXXXX, 
        registry=threading.local()
    }
}

class  scoped_session:
    def add(self, *args, **kwargs):
        return getattr(self.registry(), 'add')(*args, **kwargs)
        
    def add_all(self, *args, **kwargs):
        return getattr(self.registry(), 'add_all')(*args, **kwargs)
    
    def commit(self, *args, **kwargs):
        return getattr(self.registry(), 'commit')(*args, **kwargs)
        
    def query(self, *args, **kwargs):
        return getattr(self.registry(), 'query')(*args, **kwargs)
"""
session = scoped_session(XXXXXX)
def task():

    # 1. 原来的session对象 = 执行session.registry()
    # 2. 原来session对象.query
    data = session.query(models.Classes).all()
    print(data)
    session.remove()

    # 1. 原来的session对象 = 执行session.registry()
    # 2. 原来session对象.query
    data = session.query(models.Classes).all()
    print(data)
    session.remove()

for i in range(10):
    t = Thread(target=task)
    t.start()
