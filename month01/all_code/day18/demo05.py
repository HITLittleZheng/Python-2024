"""
    内置高阶函数

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
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1002, 9001, "孙悟空", 120000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 需求:获取所有员工姓名
# IterableHelper.select()
# map:映射
for name in map(lambda e:e.name,list_employees):
    print(name)

# 需求:获取所有月薪小于20000的员工
# IterableHelper.find_all()
# filter:筛选器
for emp in filter(lambda item:item.money < 20000,list_employees):
    print(emp.__dict__)

# 需求:获取所有月薪最小的员工
# IterableHelper.get_max()
# min:最小 max:最大
emp = min(list_employees,key = lambda e:e.money)
print(emp.__dict__)

# sorted 排序:
# 注意：返回新列表,不改变原有列表
# - 升序排列
new_list = sorted(list_employees,key =lambda e:e.did )
# - 降序排列
new_list = sorted(list_employees,key =lambda e:e.did,reverse=True)
for item in new_list:
    print(item.__dict__)

# 注意：修改原列表
list_employees.sort(key =lambda e:e.did )

