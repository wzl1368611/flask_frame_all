import redis


conn = redis.Redis()

conn.hscan_iter()