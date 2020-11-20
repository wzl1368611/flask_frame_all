from types import MethodType,FunctionType

class Foo(object):
    def fetch(self):
        pass

print(isinstance(Foo.fetch,MethodType))
print(isinstance(Foo.fetch,FunctionType)) # True

obj = Foo()
print(isinstance(obj.fetch,MethodType)) # True
print(isinstance(obj.fetch,FunctionType))