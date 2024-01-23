"""
练习01
假设一个目录中有若干文本文件,编写一个
程序,将这些文本文件合并为一个大文件:union.txt
放在当前程序所在文件夹

提示: os.listdir() 获取目录下文件名
     每个文件逐个复制到 union.txt中即可
"""
import os

dir = "/home/tarena/FTP/"

fw = open("union.txt", "w")

# 每次获取一个文件名
for file in os.listdir(dir):
    fr = open(dir + file, "r")
    fw.write(fr.read())  # 复制一个文件
    fr.close()

fw.close()
