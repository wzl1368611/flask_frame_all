
class Foo(object):
    pass

for i in ['k1','k2']:
    setattr(Foo,i,lambda self:1)

obj = Foo()
v = obj.k1()
print(v)