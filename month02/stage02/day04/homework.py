"""
编写一个程序,循环不停的写入
日志 (my.log)。每2秒写入一行,
要求每写入一行都要显示出来。
结束程序后（强行结束）,
重新运行要求继续往下写，序号衔接

1. Mon Nov 29 18:04:02 2021
2. Mon Nov 29 18:04:04 2021
3. Mon Nov 29 18:08:16 2021
4. Mon Nov 29 18:08:18 2021

提示: time.ctime() 获取当前时间
     time.sleep(2) 时间间隔
"""
import time

# 打开文件 : 追加
log = open("my.log","a+",buffering=1)

# 文件偏移量放到开头
log.seek(0,0)

n = len(log.readlines()) + 1  # 序号 = 行数 + 1
while True:
    msg = "%d. %s\n"%(n,time.ctime())
    log.write(msg)
    time.sleep(2) # 暂停2s
    n += 1










