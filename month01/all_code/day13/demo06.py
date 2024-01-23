"""
    算数运算符重写
        每个运算符都有对应的方法
            例如:+ 对应 __add__
        在函数中,若要根据不同类型执行不同代码,需要判断关系.
            例如:判断参数是向量
                if type(参数) == 向量
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 决定两个自定义对象相加的逻辑
    def __add__(self, other):
        # 判断传入的数据other是向量还是数值??
        if type(other) == Vector2:
            # 向量+向量
            x = self.x + other.x
            y = self.y + other.y
        else:
            # 向量+数值
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
pos04 = pos01 + 10
print(pos03.__dict__)
