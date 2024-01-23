"""
    迭代器
"""


# 自定义对象参与for循环
class StudentIterator:  # 迭代器
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index >= len(self.data) - 1:
            raise StopIteration()
        self.index += 1
        return self.data[self.index]


class StudentController:  # 可迭代对象
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        return StudentIterator(self.list_student)


controller = StudentController()
controller.list_student.append("吉宇轩")
controller.list_student.append("周字华")
controller.list_student.append("涂洋涛")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
