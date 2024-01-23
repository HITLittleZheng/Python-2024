"""
os 模块函数操作文件
"""
import os

# 单位字节
print("文件大小:",os.path.getsize("my.log"))

print("获取文件名:",os.listdir("."))

print("文件是否存在:",os.path.exists("my.log"))

# 删除文件
os.remove("my.log")