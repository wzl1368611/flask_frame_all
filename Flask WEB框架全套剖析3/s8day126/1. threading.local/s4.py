from threading import get_ident,Thread
import time

storage = {}
def set(k,v):
    ident = get_ident()
    if ident in storage:
        storage[ident][k] = v
    else:
        storage[ident] = {k:v}

def get(k):
    ident = get_ident()
    return storage[ident][k]




def task(arg):
    set('val',arg)
    v = get('val')
    print(v)

for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()