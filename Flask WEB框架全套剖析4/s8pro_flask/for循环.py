class Foo(object):

    def __iter__(self):
        # 返回迭代器
        # return iter([11,22,33,44])
        # 返回生成器（特殊的迭代器）
        yield 1
        yield 2
        yield 3


obj = Foo()

for item in obj:
    print(item)