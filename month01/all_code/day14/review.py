"""
    复习-mvc
        1. mvc架构
            m:多个数据封装为一个数据
            v:负责界面逻辑,输入输出
            c:负责核心业务逻辑
        2. 类变量
            model的全球唯一标识符使用类变量才能保持唯一性
        3. 封装
            私有化:隐藏实现细节,对外提供必要功能
            属性:controller的列表提供只读属性
        4. 重写
            直接打印自定义对象:要重写对象的__str__
            print(自定义对象)

            自定义对象列表排序:需要重写对象的__lt__
            list_data.sort()

            自定义对象列表移除:需要重写对象的__eq__
            list_data.remove()
"""


class Model:
    """
        xx模型:多个数据封装为一个数据
    """

    def __init__(self, data01=0, data02=0, data03=0):
        self.data01 = data01
        self.data02 = data02
        self.data03 = data03

    def __str__(self):
        return str(self.__dict__)

class View:
    """
        xx视图:负责界面逻辑,输入输出
    """

    def __init__(self):
        self.controller = Controller()

    def __display_data(self):
        for item in self.controller.list_data:
            # 直接打印自定义对象:要重写对象的__str__
            print(item)

            # 自定义对象列表排序:需要重写对象的__lt__
            # self.controller.list_data.sort()

            # 自定义对象列表移除:需要重写对象的__eq__
            # self.controller.list_data.remove()


    def __input_data(self):
        # 录入多个信息
        model = Model()
        model.data01 = int(input("请输入第1个数据:"))
        model.data02 = int(input("请输入第2个数据:"))
        self.controller.add_data(model)

    def main(self):
        self.__input_data()
        self.__display_data()

class Controller:
    """
        控制器:负责核心业务逻辑
    """
    start_id = 1001

    @classmethod
    def set_id(cls, new):
        new.data03 = cls.start_id
        cls.start_id += 1

    def __init__(self):
        self.__list_data = []

    @property
    def list_data(self): # 只读数据:让view可以读取私有变量
        return self.__list_data

    def add_data(self, new):
        Controller.set_id(new)
        self.__list_data.append(new)

view = View()
view.main()