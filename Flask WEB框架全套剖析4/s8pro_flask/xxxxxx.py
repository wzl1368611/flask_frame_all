# from flask.sessions import SecureCookieSessionInterface
#
# import datetime
#
# v = datetime.datetime.now()
# h = datetime.timedelta(hours=1)
# new_date = v + h
# print(new_date)

from redis import Redis


conn = Redis(host='127.0.0.1')
v = conn.keys()
print(v)