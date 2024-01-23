"""
在主目录下有一个文件夹，里面有若干普通文件，
要求将该文件夹复制一份到当前程序所在目录下，
在复制过程中要求每个文件的复制过程采用一个独立
的进程完成

提示： 创建文件夹 os.mkdir(dir)
"""
from multiprocessing import Process
import os

copy_dir = "/home/tarena/FTP/"
new_dir = "./FTP/"


# 复制文件  --》 所有子进程
def copy(filename):
    fr = open(copy_dir+filename,'rb')
    fw = open(new_dir+filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


def main():
    os.mkdir(new_dir)  # 创建文件夹
    # 遍历文件列表
    for file in os.listdir(copy_dir):
        # 创建子进程
        p = Process(target=copy,args=(file,))
        p.start()

if __name__ == '__main__':
    main()



