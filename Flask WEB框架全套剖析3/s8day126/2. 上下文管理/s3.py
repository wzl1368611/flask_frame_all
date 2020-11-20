class Foo(object):
    def __init__(self):
        self.__age = 18


obj = Foo()
v = obj._Foo__age
print(v)