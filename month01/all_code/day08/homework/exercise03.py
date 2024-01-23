"""
    4. (选做)在列表中删除所有偶数
        list01 = [10,20,33,40,51,60,70,80]
       提示:倒序删除
"""
# 需求：根据条件删除多个元素
list01 = [10, 20, 33, 40, 51, 60, 70, 80]

# 漏删：索引向后,元素向前
# 越界：删除前确定最大索引,但随着删除过程会减少
# for i in range(len(list01)):# 0 1 2 3.. 7
#     if list01[i] % 2 ==0:
#         del list01[i]

# 解决方案：倒序删除
for i in range(len(list01) - 1, -1, -1):
    if list01[i] % 2 == 0:
        del list01[i]
print(list01)