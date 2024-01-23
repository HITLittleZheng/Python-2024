"""
随堂练习：大文件拆分
有一个大文件，将其拆分成上下两个部分 （按照字节大小）
，要求两个部分拆分要同步进行
plus ： 假设文件很大不要一次read读取全部

提示 ： os.path.getsize() 获取文件大小

思路： 上半部分函数--》 文件复制
      下半部分函数
      创建用进程分别调用这连个函数
"""
from multiprocessing import Process
import os

filename = "/home/tarena/下载/dili.jpeg"
size = os.path.getsize(filename)

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open("top.jpeg",'wb')
    n = size // 2  # 一半字节数
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    fw.write(fr.read(n)) # 复制剩下的
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpeg", 'wb')
    fr.seek(size // 2) # 文件偏移到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

def main():
    p = Process(target=top)  # 子进程上半部分
    p.start()
    bot() # 下半部分
    p.join() # 确保子进程完成
    print("拆分完成")

if __name__ == '__main__':
    main()







