
class Foo(object):
    CITY = 'bj'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def func(self):
        pass

# print(Foo.CITY)
# print(Foo.func)
print(Foo.__dict__)
print(dir(Foo))
# obj1 = Foo('oldboy',54)
# print(obj1.__dict__)