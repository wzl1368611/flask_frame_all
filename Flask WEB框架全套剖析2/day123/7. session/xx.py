# 情况一：
# class Foo(object):
#     def __setitem__(self, key, value):
#         pass
#
# obj = Foo()
# obj['xxx'] = 123 # __setitem__
# 情况二：

class Foo(dict):
    pass

obj = Foo()