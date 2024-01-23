from usl import StudentView

# 快捷键:main+回车
if __name__ == '__main__': 
    # 如果是主模块,才执行当前启动代码
    # (如果被导入,不启动)
    view = StudentView()
    view.main()