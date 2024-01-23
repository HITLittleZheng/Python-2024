"""
    学生信息管理系统
        练习1:将CommodityController中start_id,
            由实例变量改为类变量;
            由类方法操作类变量
            多个对象互相影响-->大家数据-->类变量
            多个对象互不影响-->自己数据-->实例变量
        练习2:对商品信息管理系统进行封装
            对外提供必要的功能,隐藏实现的细节.
            view:对外提供,main
            controller:添加/移除/修改
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid


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
            print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")

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
        self.list_student = []

    def add_student(self, new_stu):
        StudentController.__set_student_id(new_stu)
        self.list_student.append(new_stu)

    def remove_student(self, sid):
        for i in range(len(self.list_student)):
            if self.list_student[i].sid == sid:
                del self.list_student[i]
                return True
        return False  # 如果没有找到则删除失败

    def update_student(self, stu):
        for item in self.list_student:
            if item.sid == stu.sid:
                # item.name = stu.name
                # item.age = stu.age
                # item.score = stu.score
                item.__dict__ = stu.__dict__
                return True
        return False


# -------------入口---------------
# 在类外调用实例方法,使用自定义对象名
#   类内              self
view = StudentView()
view.main()

