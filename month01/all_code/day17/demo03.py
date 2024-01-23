"""
    zip
"""
list_name = ["张无忌","赵敏","周芷若"]
list_room = [101,102,103]
# (第一个列表元素,第二个列表元素)
for item in zip(list_name,list_room):
    print(item)

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]
# new_map = []
# for item in zip(map[0],map[1],map[2],map[3]):
#     new_map.append(list(item))
# print(new_map)

# new_map = []
# for item in zip(*map):
#     new_map.append(list(item))
# print(new_map)

new_map = [list(item)for item in zip(*map)]
print(new_map)

# 练习：使用学生列表封装以下三个列表中数据
# list_student_name = ["悟空", "八戒", "白骨精"]
# list_student_age = [28, 25, 36]
# list_student_sex = ["男", "男", "女"]
# list_student= [StudentModel("悟空",28,"男")...]
