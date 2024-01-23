"""
练习０１： 使用dict.txt完成
编写一个函数:query_word
参数传入一个单词，调用函数在单词本查询这个单词
返回值是单词对应的那一行内容
提示：单词本每行一个单词
　　　单词按从小到大排列
　　　单词解释之间有空格
     split()
"""

# def query_word(word):
#     fr = open("dict.txt") #　读打开
#     # 逐行读取
#     n = len(word)
#     for line in fr:
#         if line[:n] == word and line[n] == " ":
#             return line

def query_word(word):
    fr = open("../day10/dict.txt") #　读打开
    # 逐行读取
    for line in fr:
        tmp = line.split(' ') # 按照空格分割
        if tmp[0] > word:
            break # 如果遍历的单词已经大于目标则停止查找
        elif tmp[0] == word:
            fr.close()
            return line
    fr.close()

print(query_word("abc"))












