"""
     画出下列代码内存图
"""
class MyClass:
    # 将类变量定义在代码区中
    data02 = 20
    def __init__(self):
        self.data01 = 10
        self.data01 += 1
        MyClass.data02 += 1

# data01:10 --> 11
# data02:20 --> 21
m01 = MyClass()
# data01:10 --> 11
# data02:21 --> 22
m02 = MyClass()
# data01:10 --> 11
# data02:22 --> 23
m03 = MyClass()
print(m03.data01) # 11
print(MyClass.data02) # 23
