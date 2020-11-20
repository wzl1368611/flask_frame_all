class A(object):
    pass


class B(A):
    pass


class C(object):
    pass

class D(B,C):
    pass

print(D.__mro__)




