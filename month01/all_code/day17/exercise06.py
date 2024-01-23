"""
    需求：
    定义函数，在员工列表中查找所有编号是1003的员工
    定义函数，在员工列表中查找所有姓名是孙悟空的员工
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def find_all01():
    for item in list_employees:
        if item.eid == 1003:
            yield item

def find_all02():
    for item in list_employees:
        if item.name == "孙悟空":
            yield item

for item in find_all01():
    print(item.__dict__)

def condition01(emp):
    return emp.eid == 1003

def condition02(element):
    return element.name == "孙悟空"

def find_all(condition):
    for item in list_employees:
        # if item.name == "孙悟空":
        # if condition02(item):
        if condition(item):
            yield item

for item in find_all(condition01):
    print(item.__dict__)