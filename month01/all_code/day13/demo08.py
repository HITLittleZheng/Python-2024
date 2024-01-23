"""
    比较运算符重写　
"""


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 决定对象相同的依据
    def __eq__(self, other):
        # 默认:比较对象的地址
        # return id(self) == id(other)
        # 修改:比较对象的内容
        # return self.x == other.x and self.y == other.y
        return self.__dict__ == other.__dict__

    # 决定对象大小的依据
    def __lt__(self, other):
        return self.x < other.x


pos01 = Vector2(1, 1)
pos02 = Vector2(1, 1)

print(pos01 == pos02)  # False

list01 = [
    Vector2(1, 1),
    Vector2(2, 2),
    Vector2(3, 3),
    Vector2(4, 4),
    Vector2(5, 5),
]
# 以下函数,内部调用的都是对象的__eq__方法
print(Vector2(1, 1) in list01)
print(list01.count(Vector2(2, 2)))
list01.remove(Vector2(3, 3))
# 以下函数,内部调用的都是对象的__lt__方法
list01.sort(reverse=True)  # 降序排列
for item in list01:
    print(item.__dict__)
