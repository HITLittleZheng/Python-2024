from bll import StudentController
from model import StudentModel

class StudentView:
    """
        学生视图:负责输入输出相关功能
    """

    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        """
            入口:一种简洁的使用方式
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
        print("4键修改学生信息")

    def __select_menu(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_student_info()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student_info(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.__controller.add_student(stu)

    def __display_students(self):
        for item in self.__controller.list_student:
            # print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")
            # 必须重写Model的__str__
            print(item)

    def __delete_student(self):
        sid = int(input("请输入学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入学生编号:"))
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")
