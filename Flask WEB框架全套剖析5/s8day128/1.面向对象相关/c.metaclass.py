# ######################################################## 创建类 ########################################################
# 1. 创建类的两种方式
"""
class Foo(object,metaclass=type):
    CITY = "bj"

    def func(self,x):
        return x + 1

Foo = type('Foo',(object,),{'CITY':'bj','func':lambda self,x:x+1})
"""

# 2. 类由自定义type创建
#    类由type创建，通过metaclass可以指定当前类由那一个type创建。
"""
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('创建类之前')
        super(MyType,self).__init__(*args,**kwargs)
        print('创建类之后')

class Foo(object,metaclass=MyType): # 当前类，由type类创建。
    CITY = "bj"
    def func(self, x):
        return x + 1
"""
# 3. 类的继承
#    类的基类中指定了metaclass，那么当前类也是由metaclass指定的类来创建当前类。
"""
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('创建类之前')
        super(MyType,self).__init__(*args,**kwargs)
        print('创建类之后')

class Foo(object,metaclass=MyType): # 当前类，由type类创建。
    CITY = "bj"
    def func(self, x):
        return x + 1

class Bar(Foo):
    pass
"""


# ################################## 变 ##################################
"""
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('创建类之前')
        super(MyType,self).__init__(*args,**kwargs)
        print('创建类之后')

Base = MyType('Base',(object,),{})
# class Base(object,metaclass=MyType):
#     pass

class Foo(Base):
    CITY = "bj"
    def func(self, x):
        return x + 1
"""
# ################################## 变 ##################################
"""
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('创建类之前')
        super(MyType,self).__init__(*args,**kwargs)
        print('创建类之后')

def with_metaclass(arg):
    return MyType('Base',(arg,),{}) # class Base(object,metaclass=MyType): pass

class Foo(with_metaclass(object)):
    CITY = "bj"
    def func(self, x):
        return x + 1
"""

# ######################################################## 实例化 ########################################################
class MyType(type):
    def __init__(self,*args,**kwargs):
        super(MyType,self).__init__(*args,**kwargs)

class Foo(object,metaclass=MyType): # 当前类，由type类创建。
    pass


"""
0. Mytype的__init__
obj = Foo() 
1. MyType的__call__
2. Foo的__new__
3. Foo的__init__
"""