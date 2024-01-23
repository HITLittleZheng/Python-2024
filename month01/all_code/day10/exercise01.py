"""
练习：创建手机类，实例化两个对象并调用其函数，最后画出内存图。
​	数据：品牌、价格、颜色
​	行为：通话
"""

# 类名:单词首字母大写,多个单词不用下划线隔开
class MobilePhone:
    # self 存储的是当前创建的对象
    def __init__(self, brand="", price=0, color=""):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "在通话")

# 创建对象自动执行__init__函数
huawei = MobilePhone("华为", 8000, "白色")
huawei.color = "黑色"
huawei.call()
iphone = MobilePhone("苹果", 7000, "银色")
iphone.call()
