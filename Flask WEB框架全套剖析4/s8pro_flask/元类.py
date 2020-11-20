
class MyType(type):

    def __call__(self, *args, **kwargs):
        pass

class Foo(object,metaclass=MyType):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass


obj = Foo()