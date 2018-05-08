
class Root(object):
    def __init__(self):
        print("this is Root")

class B(object):

    def __init__(self):
        print("enter B")
        print(self)
        super(B,self).__init__()
        print("leave B")

class C(Root):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")

class D(B,C):
    pass

d = D()
print(d.__class__.__mro__)


# def super(cls,inst):
#     mro = inst.__class__.mro()
#     return mro[mro.index(cls) + 1]

# 1. inst 负责生成 MRO 的 list
# 2. 通过 cls 定位当前 MRO 中的 index, 并返回 mro[index + 1]
# 全称 Method Resolution Order
#在 MRO 中，基类永远出现在派生类后面，如果有多个基类，基类的相对顺序保持不变。