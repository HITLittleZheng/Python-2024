"""
    索引 index
        容器名[索引值]
            索引值要求为整数

        注意边界问题：
            IndexError: string index out of range
"""

s = "Python"

# 正向索引
print(s[0])
print(s[1])
print(s[3])

# 反向索引：
print(s[-1])
print(s[-3])

# 注意：边界问题
# print(s[6]) # IndexError: string index out of range

# 通过索引进行遍历
for item in range(6):
    print(s[item])

# 扩展：获取容器长度
# len()
print(len(s))  # 6

print('---------')
for item in range(len(s)):
    print(s[item])
