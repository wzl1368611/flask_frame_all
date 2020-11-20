# 1. 为什么要用装饰器？
"""
在不改变原函数的基础上，对函数执行前后进行自定义操作。
"""
import functools

def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
"""
1. 执行wapper函数，并将被装饰的函数当做参数。 wapper(index)
2. 将第一步的返回值，重新赋值给  新index =  wapper(老index)
"""
@wapper
def index(a1):
    return a1 + 1000

@wapper
def order(a1):
    return a1 + 1000


print(index.__name__)
print(order.__name__)




