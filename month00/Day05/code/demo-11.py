"""
    列表：
        遍历：
            正向遍历：
                for 变量 in 非空列表:
                    循环体

                for 索引值 in range(len(非空列表)):
                    循环体

            反向遍历：
                for 索引值 in range(len(非空列表)-1, -1, -1):
                    循环体
"""

list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 1. 正向遍历
# for 变量 in 非空列表:
#     循环体

for i in list_01:
    print(i)

# for 索引值 in range(len(非空列表)):
#     循环体
for index in range(len(list_01)):
    print(list_01[index])

print('-' * 50)

# 2. 反向遍历
# for 索引值 in range(len(非空列表)-1, -1, -1):
#     循环体
for index in range(len(list_01) - 1, -1, -1):
    print(list_01[index])
