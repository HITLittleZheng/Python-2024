"""
    学生信息管理系统
        餐厅架构
            迎宾--服务员--厨师--传菜员--收银员

        软件架构
            View--Controller--Model
            表面      核心     打包
           输入输出  添加删除  姓名年龄...
"""


# 练习1:创建商品信息管理系统
# 以需求为导向:
# 1. 显示菜单
# 2. 添加信息
#      view:录入信息
#      model:包装信息(商品名称,单价,编号)
#      controller:编号,追加
# 练习2:
# 3. 显示信息
#    view:输出信息
# 3. 删除信息
#    view:获取编号/输出成败
#    controller:从列表移除数据
# 练习3:
# 4. 修改信息
#    view:获取信息/输出成败
#    controller:从列表中定位元素修改实例变量
class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 由系统决定的全球唯一标识符,用于标记信息
        self.sid = sid


class StudentView:
    """
        学生视图:负责输入输出相关功能
    """

    def __init__(self):
        self.controller = StudentController()

    def display_menu(self):
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
        print("4键修改学生信息")

    def select_menu(self):
        item = input("请您输入选项:")
        if item == "1":
            self.input_student_info()
        elif item == "2":
            self.display_students()
        elif item == "3":
            self.delete_student()
        elif item == "4":
            self.modify_student()

    def input_student_info(self):
        # 用一个Model包装多个数据
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        # stu.sid 由controller负责赋值
        self.controller.add_student(stu)

    def display_students(self):
        for item in self.controller.list_student:
            print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")

    def delete_student(self):
        sid = int(input("请输入学生编号:"))
        if self.controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入学生编号:"))
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        if self.controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")


class StudentController:
    """
        学生控制器:负责管理所有学生,提供核心功能.
    """

    def __init__(self):
        self.list_student = []
        self.start_id = 1001

    def add_student(self, new_stu):
        # 自增长
        new_stu.sid = self.start_id
        self.start_id += 1
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
while True:
    view.display_menu()
    view.select_menu()
