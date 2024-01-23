"""
    有一家公司有如下几种岗位:
        -- 程序员:底薪 + 项目分红
        -- 测试员:底薪 + Bug数*5
        -- ...
    创建员工管理器:
        -- 记录所有员工
        -- 计算所有员工总薪资
    封装:程序员/测试员/员工管理器
    继承:创建员工类,隔离员工管理器与程序员和测试员的变化
    多态:程序员/测试员重写员工类的计算薪资方法
"""


# ---------------架构师---------------
class EmployeeController:
    def __init__(self):
        self.list_employee = []

    def get_total_salary(self):
        total_salary = 0
        for item in self.list_employee:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def calculate_salary(self):
        pass


# ---------------程序员---------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def calculate_salary(self):
        return self.base_salary + self.bug_count * 5


# ---------------测试---------------
controller = EmployeeController()
controller.list_employee.append(Programmer(10000, 1000000))
controller.list_employee.append(Tester(5000, 2))
print(controller.get_total_salary())
