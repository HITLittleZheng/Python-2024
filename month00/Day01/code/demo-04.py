"""
    基本输出语句：
        print(value, sep=" ", end="\n")
"""
print("hello world")

# sep 参数： 多个值之间的分隔符, 默认为 空格 " "
print("hello", "world", "!")
# sep="" 表示将多个值之间的分隔符删除
print("hello", "Python", "hello", "...", sep="")
# sep="--->" 表示将多个值之间的分隔符变为 --->
print("hello", "Python", "hello", "...", sep="--->")

print('*' * 50)
# end="\n" 输出完毕之后会自动的在末尾追加一个字符串，
#           默认为"\n" 表示换行
print("键盘敲烂", end=" ")
print("薪资过万")

# 脱单
# 不脱发
print("脱单", end=",")
print("不脱发")
