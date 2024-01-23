"""
    迭代器 --> yield
"""


class StudentController:
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        # 生成迭代器代码的大致规则:
        # 1. 将yield以前的代码作为__next__方法体
        # 2. 将yield以后的数据作为__next__返回值
        index = 0
        yield self.list_student[index]

        index += 1
        yield self.list_student[index]

        index += 1
        yield self.list_student[index]

        # raise StopIteration()


controller = StudentController()
controller.list_student.append("吉宇轩")
controller.list_student.append("周字华")
controller.list_student.append("涂洋涛")
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
