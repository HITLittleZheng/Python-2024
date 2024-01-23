"""
    小结-容器
        1. 种类与特征
            字符串str：存储字符编码,不可变,序列
            列表list：存储变量,可变,序列
            元组tuple：存储变量,不可变,序列

            字典dict：存储键值对,可变,散列
                键唯一且不可变(数值/字符串/元组)
            集合set：存储键,可变,散列

        2. 可变性
            可变:预留空间+自动扩容
                优点：操作方便(增删改)
                缺点：占用内存空间较多

            不可变:按需分配
                优点：占用内存空间较少
                缺点：操作不方便(不能增删改)
                适用性：优先

        3. 序列与散列
            序列：有顺序,定位灵活(支持索引切片),内存空间占用较少
            散列：无顺序,定位单个元素最快,内存空间占用较多
"""
# 4. 基础操作
# 创建
list01 = [10, 20, 30]
list02 = list("悟空")

dict01 = {"name": "悟空", "age": 26}
dict02 = dict([("name", "悟空"), ("age", 26)])

# 添加
list01.append(40)
list01.insert(0, 50)

dict01["money"] = 10000000

# 定位
print(list01[0])
print(list01[:2])
print(list01[-2:])

# 将右侧元素依次取出,存入左侧定位的区域
list01[:] = ["a", "b", "c"]
# 变量list01存储了新列表,取消与旧列表的关联
list01 = ["a", "b", "c"]

# 将list02浅拷贝出新列表赋值给变量list01
list01 = list02[:]
# 将list02存储的列表地址赋值给变量list01
list01 = list02

# 右侧浅拷贝出新列表,依次取出元素给左侧列表元素赋值
list01[:] = list02[:]

print(dict01["name"])

# 遍历
for item in list01:
    print(item)

for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for key, value in dict01.items():
    print(key)
    print(value)

# 删除
# -- 根据定位删除
del list01[0]
del list01[:3]
# -- 根据元素删除(如果有重复也只删除第一个)
list01.remove(10)

del dict01["name"]
