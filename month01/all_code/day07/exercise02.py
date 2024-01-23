"""
    二维列表-操作

"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# 1)
# print(list01[0][0])
# print(list01[0][1])
# print(list01[0][2])
# print(list01[0][3])
# print(list01[0][4])
# for c in range(5):
#     print(list01[0][c])
for c in range(len(list01[0])):
    print(list01[0][c])

# 2)
# print(list01[1][4])
# print(list01[1][3])
# print(list01[1][2])
# print(list01[1][1])
# print(list01[1][0])
# for c in range(4,-1,-1):
#     print(list01[1][c])
for c in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][c])

# 3)
# print(list01[0][2])
# print(list01[1][2])
# print(list01[2][2])
for r in range(len(list01)):
    print(list01[r][2])

# 4)
# print(list01[2][3])
# print(list01[1][3])
# print(list01[0][3])
for r in range(len(list01) - 1, -1, -1):
    print(list01[r][3])

# 5)
# for c in range(len(list01[0])):
#     print(list01[0][c],end = " ")
# print()
# for c in range(len(list01[1])):
#     print(list01[1][c],end = " ")
# print()
# for c in range(len(list01[2])):
#     print(list01[2][c],end = " ")
# print()

for r in range(len(list01)):
    for c in range(len(list01[r])):
        print(list01[r][c], end="\t")
    print()

# for line in list01:
#     for item in line:
#         print(item, end="\t")
#     print()
