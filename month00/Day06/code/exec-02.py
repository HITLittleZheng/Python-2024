"""
    单词翻转
        输入： How are you
        输出： you are How
"""
data = input("请输入一句话：")
list_map = data.split()
res = ' '.join(list_map[::-1])
print(res)