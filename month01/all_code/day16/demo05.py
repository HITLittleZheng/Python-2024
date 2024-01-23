"""
    异常-处理
        价值:保障程序能够按照既定的流程执行,不紊乱.
"""


# 1. 包治百病
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print(f"每人{result}个苹果")
    # except Exception:
    except:
        print("程序出错啦")

div_apple(10)

# 2. 对症下药(官方建议)
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print(f"每人{result}个苹果")
    except ValueError:
        print("错误!输入了非整数.")
    except ZeroDivisionError:
        print("错误!输入了零.")

div_apple(10)
"""

# 3. 无论是否发生异常.一定执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print(f"每人{result}个苹果") 
        # 文件操作
        #   -- 打开
        #   -- 处理 
    finally:
        #   -- 关闭
        print("分苹果结束")

div_apple(10)
"""

# 4. 只有程序没有发生错误才执行了逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print(f"每人{result}个苹果")
    except ValueError:
        print("程序出错了")
    else:
        print("分苹果成功")

div_apple(10)
"""
print("后续逻辑")
