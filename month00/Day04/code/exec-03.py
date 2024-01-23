"""
    输入两个数, 分别代表起始值 和 终止值.
    根据 输入值大小,可以升序 或 降价打印输入。
    起始值： 1
    终止值: 10
    打印为: 1 2 3 4 5 6 7 8 9 10

    打印为: 10 9 8 7 6 5 4 3 2 1
"""
start = int(input("请输入起始值:"))
end = int(input("请输入终止值:"))

# while start <= end:
#     print(start, end=" ")
#     start += 1


while start <= end:
    print(end, end=" ")
    end -= 1
