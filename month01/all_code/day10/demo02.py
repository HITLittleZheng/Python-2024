"""
    实例成员
        实例变量:用于表达不同个体的不同数据
            对象.变量名
        实例方法(函数):操作实例变量
            def 方法名(self,参数):
                ...

            对象.方法名(数据)
"""
# 面向过程的全局变量,在内存中只有一份
name = "双儿"
name = "阿珂"


class Wife:
    def __init__(self, name=""):
        # 创建实例变量:每个对象都存储一份
        self.name = name
        self.work()

    # 创建实例方法
    def work(self):
        print("在工作")

jian_ning = Wife("建宁")
# 修改实例变量
jian_ning.name = "公主"
# 读取实例变量
print(jian_ning.name)
# 内置实例变量__dict__:存储了对象的所有实例变量
print(jian_ning.__dict__) # {'name': '公主'}
jian_ning.work() # 通过对象调用实例方法

# 建议将创建实例变量的代码放在类中
"""
class Wife:
    pass

jian_ning = Wife()
# 创建实例变量
jian_ning.name = "公主"
# 修改实例变量
jian_ning.name = "建宁公主"
# 读取实例变量
print(jian_ning.name)
"""

# 建议将创建实例变量的代码放在__init__中
"""
class Wife:
    def set_name(self, name):
        self.name = name  # 创建实例变量


jian_ning = Wife()
jian_ning.set_name("建宁")
# 读取实例变量
print(jian_ning.name)
"""
