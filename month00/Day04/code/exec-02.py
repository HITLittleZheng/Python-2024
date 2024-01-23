"""
    循环录入五个成绩, 最后打印平均成绩
"""

count = 0
total_score = 0
while count < 5:
    score = float(input("请输入成绩："))
    count += 1

    total_score += score

print('平均成绩为：', total_score / 5)
