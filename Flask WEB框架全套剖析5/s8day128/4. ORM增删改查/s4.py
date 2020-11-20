import models

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine =create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/s8day128db?charset=utf8")
XXXXXX = sessionmaker(bind=engine)
session = XXXXXX()

# 改
session.query(models.Classes).filter(models.Classes.id > 0).update({models.Classes.name: models.Classes.name + "099"}, synchronize_session=False)

session.commit()

session.close()
