"""
	练习：创建对象计数器，统计构造函数执行的次数，
		使用类变量实现并画出内存图。
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.count}个老婆")

    def __init__(self, name):
        Wife.count += 1
        # 实例变量:不同对象不同信息
        self.name = name


# 每个对象存储一份实例变量
# 类中存储一份类变量
w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
Wife.print_count()  # 总共娶了5个老婆
