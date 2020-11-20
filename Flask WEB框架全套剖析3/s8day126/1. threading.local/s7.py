from threading import get_ident,Thread
import time


class Local(object):
    storage = {}

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return Local.storage[ident][k]


obj = Local()

def task(arg):
    obj.val = arg
    print(obj.val)

for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()