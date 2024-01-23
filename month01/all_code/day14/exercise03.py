"""

"""


# ---------------架构师---------------
class EmployeeController:
    def __init__(self):
        self.__list_employee = []

    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.__list_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__list_employee:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# ---------------程序员---------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        return super().calculate_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        # self.base_salary = base_salary
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        # return self.base_salary + self.bug_count * 5
        return super().calculate_salary() + self.bug_count * 5


# ---------------测试---------------
controller = EmployeeController()
controller.add_employee(Programmer(10000, 1000000))
controller.add_employee(Tester(5000, 2))
controller.add_employee("大爷")
print(controller.get_total_salary())
