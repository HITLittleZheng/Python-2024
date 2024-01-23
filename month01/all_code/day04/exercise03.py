"""
    循环录入编码值打印文字，直到输入空字符串停止。
    效果：
    请输入数字：113
    q
    请输入数字：116
    t
    请输入数字：
    Process finished with exit code 0
"""
while True:
    str_number = input("请输入数字:")
    # if str_number == "":
    if not str_number:
        break
    int_number = int(str_number)
    print(chr(int_number))
