"""
文件读写缓冲
"""

# 行缓存
# fw = open("file.txt","w",buffering=1)

# 设置缓冲大小 10字节
fw = open("file.txt","wb",buffering=10)

while True:
    msg = input(">>")
    if not msg:
        break
    fw.write(msg.encode())
    # fw.flush() # 主动刷新 ctrl-s

fw.close()