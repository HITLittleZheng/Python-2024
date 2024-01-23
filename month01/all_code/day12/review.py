"""
    复习-MVC
        1. 软件架构
            View:负责软件界面逻辑,输入输出
                例如:录入学生信息(input)
            Controller:负责软件核心业务逻辑,添加删除
                例如:添加学生信息(分配id,存储)
            Model:负责包装多种数据,为V/C传递数据更简洁
        2. 跨类调用语法
"""
class View:
    def __init__(self):
        # "桥"
        self.controller = Controller()

    def func01(self):
        print("func01执行了")
        # 在同类中,通过self调用实例方法
        self.func03()
        # 在跨类中,通过自定义对象名调用实例方法
        self.controller.func02()

    def func03(self):
        print("func03执行了")

class Controller:
    def func02(self):
        print("func02执行了")

view = View()
view.func01()
