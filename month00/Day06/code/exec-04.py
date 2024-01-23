"""
    循环录入多个学生姓名、学生兴趣爱好[多个爱好],如果姓名为空则停止,最后打印所有信息.
        存储结构：
            {'学生姓名1': [爱好1, 爱好2], '学生姓名2':[爱好1]}

    总结小经验:
        1. 分析需求
        2. 基础的编码
            逐步书写　写一步调一步
            可能会出现异常(Error 达不到预期效果)
                --> DEBUG 调试模式(debugger 中的变量)
        3. 完善代码

    技术点:
        循环:
            while 循环:
                不知道循环次数的时候使用while 循环;
                死循环: 条件一直成立,一直执行循环体;
                一般　if 语句　结合 break　语句　退出死循环

            for 循环:
                知道循环次数的时候使用for 循环;
                可迭代对象: 能够依次获取元素
                range():

        终止循环: break 语句　终止本层循环
        跳过循环: continue 语句　跳过本次循环,进入下一次循环
        条件判断: 有选择性的执行语句

        列表:　由一系列变量组成的可变序列容器
            创建列表:
                列表名 = []
                列表名 = ["元素1", "元素2"]
            定位:
                索引:  定位单个元素
                    列表名[整数]
                    如果索引值超过范围, 则触发IndexError
                切片:　截取多个元素
                    列表名[ [起始索引]:[终止索引] [:步长] ]
            修改：
                单个修改：
                    列表名[整数]　= 值
                多个修改：
                    列表名[ [起始索引]:[终止索引] [:步长] ]　= 多个值
            删除：
                列表名.remove(元素) # 元素不存在则出发异常
                列表名.pop(index=-1)
            增加：
                列表名.append(元素) # 追加
                列表名.insert(index, value)
            遍历：
                正向遍历:
                    for 变量　in 非空列表:
                        循环体

                    for 索引值 in range(len(非空列表)):
                        循环体

                反向遍历:
                    for 索引值　in range(len(非空列表)-1, -1, -1):
                        循环体

        字符串方法：
            str.方法([参数]...)
            str.strip() 去除字符串两侧空格
            str.split() 将字符串以某种分隔符进行分割.默认为空格,返回值：list
            str.join(iterable) 以字符串连接可迭代对象, 返回值为: str
            str.replace(old, new) 字符串中　以new 替换old
        内置函数:
            len()
            max()
            min()
            sum()

        字典:　由一系列　键值对　组成的可变散列容器.
            键：　不可变类型且唯一[str int float bool ...]
            值：　可重复

            创建：
                字典名 = {键:　值}

            获取：
                字典名[键]　　键不存在则触发KeyError
                字典名.get(键, 默认值)　键不存在　默认返回None

            修改:
                字典名[键] = 值　键存在则修改; 键不存在则创建
                字典名.setdefault(键, default=None)
                    1. 键存在则返回对应值
                    2. 键不存在则创建键值对, 值默认为None
"""

# # 版本一: 创建空字典, 将姓名作为字典的key, 值为空列表
# dict_user = {}
#
# while True:
#     name = input("姓名: ")
#     if name == "":
#         break
#
#     # 　字典名[键] = 值　　---> 往dict_user 中添加键值对　[不考虑重名]
#     dict_user[name] = []
#
#
#
#
# # 版本二
# dict_user = {}
#
# while True:
#     name = input("姓名: ")
#     if name == "":
#         break
#
#     # 　字典名[键] = 值　　---> 往dict_user 中添加键值对　[不考虑重名]
#     dict_user[name] = []
#
#     hobby = input("爱好: ")
#     if hobby == "":
#         break
#     # 通过键修改值
#     dict_user[name].append(hobby)
#
# print(dict_user)

# 版本三：

dict_user = {}
while True:
    name = input("姓名: ")
    if name == "":
        break

    # 　字典名[键] = 值　　---> 往dict_user 中添加键值对　[不考虑重名]
    dict_user[name] = []

    while True:
        hobby = input("爱好: ")
        if hobby == "":
            break

        # 通过键修改值
        dict_user[name].append(hobby)

print(dict_user)
