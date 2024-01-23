"""
    字符串字面值
"""
# 1. 双引号
data01 = "悟空"
# 2. 单引号
data02 = '悟空'
# 3. 三引号(可见即所得)
data03 = """悟空"""
data03 = '''
    悟
空'''
print(data03)
# 注意:引号冲突
print('花果山"齐天大圣"孙悟空')
print("花果山'齐天大圣'孙悟空")
print("""花果山'齐'天"大圣"孙悟空""")

# 4. 转义字符:改变原始含义特殊字符
# \"  \'   \\   \n
print("花果山\"齐天大圣\"孙悟\n空")
print("C:\\arogram Files\\bommon Files\Services")
print(r"C:\arogram Files\bommon Files\Services")

# 5. 格式化字符串:将字符串按照某个格式显示
# 语法:
# "....格式...."%(变量)
# 占位符:%s   %f   %d
name = "张三"
age = 18.6
score = 95.12345678
print(name + "的年龄是" + str(age) + ",考了" + str(score) + "分")
print("%s的年龄是%s,考了%s分" % (name, age, score))
print("%s的年龄是%d,考了%.1f分" % (name, age, score))
print("%.2d:%.2d" % (2, 3))

cure_ratio = 92
print("治愈比例为%s%%" % cure_ratio)
jin = 6
liang = 4
print("结果为：%s斤%s两" % (jin, liang))
#练习：根据下列文字，提取变量，使用字符串格式化打印信息
# 湖北确诊67802人,治愈63326人,治愈率0.99
# 70秒是01分零10秒