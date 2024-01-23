"""
    增强运算符重写
         不可变数据,+=会创建新对象
         可变数据,+=会在原对象上修改
         所以：
            __add__重写时返回新数据
            __iadd__重写时返回原数据
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # + :返回新数据
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # += :返回原数据
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

pos01 = Vector2(1, 2)
print(id(pos01))
pos01 += Vector2(3, 4)
print(id(pos01))

print(pos01.__dict__)

# 不可变数据,+=会创建新对象
# 可变数据,+=会在原对象上修改
data01 = [10, 20]
data02 = [30, 40]
print(id(data01))  # 140459663090952
data01 += data02
print(id(data01))  # 140459632590184
