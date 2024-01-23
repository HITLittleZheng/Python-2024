"""
练习02: 完成文件的复制功能
编写一个函数copy,参数有两个,第一个参数
是要复制的文件,第二个参数的一个目标文件夹
当执行函数后,将第一个参数的文件复制到,第二
个参数的指定文件夹中
"""
def copy(filename,dir):
    fr = open(filename,'rb')
    fname = filename.split('/')[-1] # 文件名字
    fw = open(dir+'/'+fname,'wb') # 拼接了打开文件的录路径
    # 边读边写
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

copy("/home/tarena/下载/yy.jpeg",".")