"""
    for-for
"""
# 2行5列
"""
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
"""

"""
for c in range(5):
    print("*",end = " ")
print() # 换行

for c in range(5):
    print("*",end = " ")
print() # 换行 
"""

# 外层循环执行1次,内层循环执行多次
#     控制行             控制列
for r in range(2):  # 0      1
    for c in range(5):  # 01234  01234
        print("*", end=" ")
    print()  # 换行 行
