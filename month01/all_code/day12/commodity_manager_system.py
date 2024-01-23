"""
    商品信息管理系统
"""


class CommodityModel:
    """
        商品模型:负责包装商品信息
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityView:
    """
        商品视图:负责商品信息的输入输出相关功能
    """

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        """
            入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1键录入商品信息")
        print("2键显示商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")

    def __select_menu(self):
        item = input("请输入您的选项:")
        if item == "1":
            # 先调用方法,再快捷键生成方法:alt+回车
            self.__input_commodity_info()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity_info(self):
        cmd = CommodityModel()
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(cmd)

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            print(f"{item.name}的编号是{item.cid},单价是{item.price}")

    def __delete_commodity(self):
        cid = int(input("请输入商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        cmd = CommodityModel()
        cmd.cid = int(input("请输入商品编号:"))
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    __start_id = 1001

    @classmethod
    def __set_commodity_id(cls, new_cmd):
        new_cmd.cid = CommodityController.__start_id
        CommodityController.__start_id += 1

    def __init__(self):
        self.list_commodity = []

    def add_commodity(self, new_cmd):
        CommodityController.__set_commodity_id(new_cmd)
        self.list_commodity.append(new_cmd)

    def remove_commodity(self, cid):
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == cid:
                del self.list_commodity[i]
                return True
        return False

    def update_commodity(self, cmd):
        for item in self.list_commodity:
            if item.cid == cmd.cid:
                item.__dict__ = cmd.__dict__
                return True
        return False


view = CommodityView()
view.main()
