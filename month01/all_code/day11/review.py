"""
    复习-面向对象
        字面意思:
            考虑软件工程问题要从对象的角度出发
            谁?干嘛?
        思考流程:
            现实世界          虚拟世界
            客观事物 -抽象化-> class 类 -实例化-> 对象
                              车牌号            京c007
                              颜色               白色
                              价格               40w
        语法:
            class 类名:
                def __init__(self,参数):
                    self.实例变量 = 参数

                def 实例方法(self,参数):
                    操作实例变量

            对象名 = 类名(数据)
            对象名.实例变量
            对象名.实例方法(数据)

        实例成员
            实例变量:表达个体的数据
            实例方法:操作实例变量
"""


# 做
class Student:
    def __init__(self, name=""):
        # 学生的姓名
        self.name = name


# 用
jmx = Student("具明星")
xtq = Student("许天奇")
# ...
# 学生列表
list_student = [
    jmx,
    xtq,
    Student("殷凌霄"),
]
list_student.append(Student("魏伟"))
