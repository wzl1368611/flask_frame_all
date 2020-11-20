from threading import Thread
from threading import local
import time
# xianglong = local()

xianglong = -1

def task(arg):
    global xianglong
    xianglong = arg
    time.sleep(2) # 亲亲翔龙
    print(xianglong)


for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()