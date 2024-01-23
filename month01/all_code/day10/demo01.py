"""
    面向过程：实现小功能
        将需求划分为多个步骤,逐一实现.
        （亲力亲为）
        思考流程：
            获取数据
            逻辑处理
            显示结果

    面向对象：设计软件架构
        将需求分配给多个人,建立交互.
        （谁?干嘛?）
        思考流程：
            现实世界        虚拟世界
        出租车 -抽象化-> 类 -具体化-> 对象
                      车牌号        京c007
                      品牌          奔驰
                      颜色          白色
                  ...

"""


# 老婆
# 数据成员：姓名/身高/颜值...
# 行为成员：工作...

# 创建类
class Wife:
    """
        抽象的老婆类
    """
    def __init__(self, name, height=160, face_score=100):
        self.name = name
        self.height = height
        # 自动生成参数快捷键:atl+回车
        self.face_score = face_score

    def work(self):
        print(self.name, "在工作")


# 创建对象,自动调用__init__函数
jian_ning = Wife("建宁", 170, 95)
jian_ning.name = "建宁公主"
jian_ning.work()

a_ke = Wife("阿珂")
a_ke.work()
# <__main__.Wife object at 0x7f49179c0f98>
print(jian_ning)

# "建宁" 是 str类的对象
#  170     int
# [10]     list
