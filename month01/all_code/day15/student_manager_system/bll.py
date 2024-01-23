from model import StudentModel


class StudentController:
    """
        学生控制器:负责管理所有学生,提供核心功能.
    """

    __start_id = 1001

    @classmethod
    def __set_student_id(cls, new_stu):
        new_stu.sid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__list_student = []

    @property  # 只读属性
    def list_student(self):
        return self.__list_student

    def add_student(self, new_stu):
        StudentController.__set_student_id(new_stu)
        self.__list_student.append(new_stu)

    def remove_student(self, sid):
        # 根据编号创建学生对象
        stu = StudentModel(sid=sid)
        if stu in self.__list_student:
            # remove函数内部调用的是元素的__eq__
            self.__list_student.remove(stu)
            return True
        return False

    def update_student(self, stu):
        for item in self.__list_student:
            if item.sid == stu.sid:
                # item.name = stu.name
                # item.age = stu.age
                # item.score = stu.score
                item.__dict__ = stu.__dict__
                return True
        return False

# 测试代码
if __name__ == "__main__":
    # 如果当前模块是主模块才执行测试代码
    # (项目交付之后,一定从main中执行)
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    for item in controller.list_student:
        print(item)
