import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='s8day127db')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor.execute("select id,name from users where name=%s and pwd=%s",['alex','123',])
cursor.execute("select id,name from users where name=%(user)s and pwd=%(pwd)s",{'user':'alex','pwd':'123'})
obj = cursor.fetchone()
conn.commit()
cursor.close()
conn.close()

print(obj)