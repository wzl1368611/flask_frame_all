from threading import Thread
from threading import get_ident

def task(arg):
    print(get_ident())


for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()