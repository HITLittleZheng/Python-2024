"""
    输入一个成绩，判断该成绩属于哪个成绩等级！
        [0, 60) 属于E级
        [60, 70) 属于D级
        [70, 80) 属于C级
        [80, 90) 属于B级
        [90, 100] 属于A级
        其他属于输入错误！
"""

score = float(input("请输入成绩： "))
# [0, 60) 属于E级
if 0 <= score < 60:
    print("E级")

# [60, 70) 属于D级
elif 60 <= score < 70:
    print("D级")

# [70, 80) 属于C级
elif 70 <= score < 80:
    print("C级")

elif 80 <= score < 90:
    print("B级")

# [90, 100] 属于A级
elif 90 <= score <= 100:
    print("A级")

# 其他属于输入错误！
else:
    print("输入错误")
