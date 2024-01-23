"""
文件处理综合训练： 使用inet.log完成
编写一个程序，输入一个端口的名称，得到这个
端口对应描述信息中的 address 值
思路： 打开文件-》read-》
根据输入名字判断在哪一段-》正则表达式匹配出地址
"""
import re

# 方法1
# data = fr.read()
# tmp = data.split("\n\n")
# for info in tmp:
#     print(info)


# 生成器--》 每次调用生成段落内容对外提供
def get_info():
    fr = open("inet.log")
    while True:
        info = ""
        for line in fr:
            if line == "\n":
                break # for
            info += line
        # 每次到这里得到了一段内容，判断是否为想要的段落
        if info:
            yield info  # 对外提供一段内容
        else:
            fr.close()
            return

def main():
    port = input("端口名称：")
    for info in get_info():
        # 正则匹配首个单词
        head = re.match("\S+",info).group()
        if port == head:
            addr = re.search("([0-9a-f]{4}\.?){3}",info).group()
            print(addr)
            return

if __name__ == '__main__':
    main()







