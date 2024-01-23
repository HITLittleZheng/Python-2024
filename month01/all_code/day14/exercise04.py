"""
    练习2：创建图形管理器
    -- 记录多种图形（圆形、矩形....）
    -- 提供计算总面积的方法.
    要求：增加新图形，不影响图形管理器.
"""


# -----------架构师---------------
class GraphicsController:
    def __init__(self):
        self.list_graphics = []

    def get_total_area(self):
        total_area = 0
        for item in self.list_graphics:
            # 编码时调用父
            total_area += item.calculate_area()
        return total_area


class Graphics:
    def calculate_area(self):
        pass

# -----------程序员---------------
class Circle(Graphics):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


class Rectangle(Graphics):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w
# -----------测试---------------

controller = GraphicsController()
controller.list_graphics.append(Circle(5))
controller.list_graphics.append(Rectangle(2,3))
print(controller.get_total_area())