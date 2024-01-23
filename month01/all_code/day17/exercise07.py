"""
    1. 在common/iterable_tools.py/IterableHelper类中
       添加2个静态方法(find_single/find_all)

    2. 创建新模块实现以下功能:
        -- 查找编号是1005的单个员工
        -- 查找部门是9001的所有员工
        -- 查找姓名是2个字的所有员工
        -- 查找薪资小于3w的第一个员工
"""
from common.iterable_tools import IterableHelper

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
# 参数:列表的元素
# 返回值:if的判断条件
def condition01(p):
    return p.eid == 1005

def condition02(e):
    return e.did == 9001

def condition03(e):
    return len(e.name) == 2

def condition04(item):
    return item.money < 30000

emp01 = IterableHelper.find_single(list_employees,condition01)
print(emp01.__dict__)

for item in IterableHelper.find_all(list_employees,condition02):
    print(item.__dict__)

for item in IterableHelper.find_all(list_employees,condition03):
    print(item.__dict__)


emp01 = IterableHelper.find_single(list_employees,condition04)
print(emp01.__dict__)