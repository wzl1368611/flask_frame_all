class Foo(object):

    def __iter__(self):
        return iter([11,22,33])


obj = Foo()