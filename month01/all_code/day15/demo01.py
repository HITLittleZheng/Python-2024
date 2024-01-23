"""
    多继承
        同名方法解析顺序
"""


class A:
    def func01(self):
        print("A-func01")

class B(A):
    def func01(self):
        print("B-func01")
        super().func01()

class C(A):
    def func01(self):
        print("C-func01")
        super().func01()

class D(B, C):
    def func01(self):
        print("D-func01")
        super().func01() # 调用的是继承列表第一个
        # C.func01(self) # 通过类名调用指定类型的同名方法

# 创建D对象
d = D()
d.func01() # D  B  C  A
