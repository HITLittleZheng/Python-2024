"""
     练习3：
     在终端中输入课程阶段数,显示课程名称
     输入：        输出：
     ​    1       	Python语言核心编程
     ​    2       	Python高级软件技术
     ​    3       	Web 全栈
     ​    4         项目实战
     ​    5         数据分析、人工智能
"""
number = input("请输入数字：")
dict_course_info = {
    "1": "Python语言核心编程",
    "2": "Python高级软件技术",
    "3": "Web 全栈",
    "4": "项目实战",
    "5": "数据分析、人工智能",
}
if number in dict_course_info:
    print(dict_course_info[number])
else:
    print("没有该阶段课程")
