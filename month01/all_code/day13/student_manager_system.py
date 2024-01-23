"""
    学生信息管理系统
        练习:封装商品控制器的列表
            --将CommodityController中的列表作为私有变量
               并添加只读属性
        练习:
            -- 直接在view中打印model对象
            -- 在controller中通过remove删除
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid

    # 直接打印当前对象所使用的格式
    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"

    # 两个学生对象,学号相同即对象相同
    def __eq__(self, other):
        return self.sid == other.sid


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


# -------------入口---------------
# 在类外调用实例方法,使用自定义对象名
#   类内              self
view = StudentView()
view.main()
