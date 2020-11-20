from threading import Thread
from threading import local
import time
from threading import get_ident
# 特殊的对象
xianglong = local()


def task(arg):
    # 对象.val = 1/2/3/4/5
    xianglong.value = arg
    time.sleep(2) # 亲亲翔龙
    print(xianglong.value)


for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()