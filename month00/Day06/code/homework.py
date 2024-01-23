"""
    循环录入学生的成绩, 如果输入为空, 则结束输入
    1. 打印所有学生的成绩
    2. 打印共有多少学生的成绩
    3. 打印最高分、最低分和平均分数
"""

score_list = []

while True:
    score = input("请输入学生成绩: ")
    if score == "":
        break

    score_list.append(float(score))

for score in score_list:
    print(score)

print(f'共有{len(score_list)}名学生的成绩')

print(f'最高分为：{max(score_list)}')
print(f'最低分为：{min(score_list)}')
print(f'平均分为：{sum(score_list) / len(score_list)}')
