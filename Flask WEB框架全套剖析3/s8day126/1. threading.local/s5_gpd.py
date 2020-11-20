from threading import get_ident,Thread
import time

storage = {}

class Gpd(object):
    def set(k, v):
        ident = get_ident()
        if ident in storage:
            storage[ident][k] = v
        else:
            storage[ident] = {k: v}

    def get(k):
        ident = get_ident()
        return storage[ident][k]

    def task(arg):
        set('val', arg)
        v = get('val')
        print(v)

    for i in range(10):
        t = Thread(target=task, args=(i,))
        t.start()


class Local(object):
    storage = {}

    def set(self,k,v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def get(self,k):
        ident = get_ident()
        return Local.storage[ident][k]

