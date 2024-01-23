"""
    练习：对数字列表进行升序排列
"""
list01 = [54, 56, 76, 7, 89]
"""
for c in range(1, len(list01)):
    if list01[0] > list01[c]:
        list01[0], list01[c] = list01[c], list01[0]
print(list01)
# [7, 56, 76, 54, 89]
for c in range(2,len(list01)):
    if list01[1] > list01[c]:
        list01[1], list01[c] = list01[c], list01[1]
print(list01)
""" 
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
