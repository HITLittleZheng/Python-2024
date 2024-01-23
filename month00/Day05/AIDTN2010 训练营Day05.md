# AIDTN2010 训练营Day05

<https://www.processon.com/view/link/61721b095653bb7318cc5bb7>

```python
"""
    一个小球从高度为100米落下, 每次弹回原高度的一半。
    计算:
        总共经过了多少米? 最终落地(最小弹起高度0.01米)
"""

height = 100

distance = height
count = 0
while height / 2 > 0.01:
    height /= 2
    count += 1
    print("第" + str(count) + '次的高度为' + str(height))
    distance += height * 2

print("共经过： ", count, '次', distance, "米")

```

## 字符串

- 由一系列字符组成的不可变序列容器，存储的是字符的编码值。

  - 字符：单个的数字，文字与符号。
  - 字节：计算机最小的存储单位是字节Bytes,等于8个位Bit。
  - 字符集：又称 码表，存储字符与二进制序列对应关系。
  - 编码：将字符转换为对应的额二进制序列的过程。
    - ASCII编码: 包含英文、数字等字符，每个字符一个字节。
    - GBK 编码: 兼容ASCII编码，包含21003个中文；英文一个字节，汉字两个字节。
    - Unicode 字符集：国际统一编码，旧字符集每个字符2个字节，新字符集4个字节。
    - UTF-8编码：Unicode的存储和传输方式，英文1个字节，中文3个字节。
  - 不可变序列：存储到数据容器中的字符不能修改。

  ```python
  # 将字符转换为 Unicode编码
  ord() # 参数为字符
  
  # 将 Unicode 编码转为 char
  chr() # 参数为整型
  ```

  ```python
  """
      转码
  """
  
  # 1. 将字符转为 Unicode
  print(ord('我'))
  print(ord('a'))
  print(ord('i'))
  print(ord('你'))
  print(ord('。'))
  
  # 2. 将 Unicode 转为 字符
  print(chr(66))
  print(chr(99))
  print(chr(25100))
  ```

### 表现形式

```python
' '
" "
''' '''
""" """

# 单引号可以嵌套双引号，双引号可以嵌套单引号
# 三引号：可以自动实现换行(换行符\n) 三引号中可以嵌套单引号 双引号；三引号可以表示多行注释, 用作文档字符串
```

### 转义字符

- 改变原有含义的特殊字符，用反斜杠 \后跟一些字符来代表特殊字符

  - | 符号 | 描述           | 符号 | 描述            |
    | ---- | -------------- | ---- | --------------- |
    | \n   | 代表换行       | \t   | 水平制表符(Tab) |
    | \r   | 返回光标至首行 | \    | 续航符          |
    | `\'` | 代表一个单引号 | `\"` | 代表一个双引号  |

- ```python
  # 原始字符串
  "c:\teacher\node\read\code"
  
  
  # r"" : 让转义字符失效
  print(r"""c:\teacher\node\read\code""")
  
  ```


### 运算符

```python
"""
    运算符
        1. 算数运算符： +  *
            + ： 用于字符串类型的拼接
            * ： 用于将字符串重复指定次数
        2. 复合赋值运算符
            += ： 表示将拼接的结果赋值给新的变量
            *= ： 将重复的指定次数赋值给新的变量
        3. 比较运算符：
            > >= < <= == !=
            规则：依据字符串中的Unicode编码依次比较两个字符串相对应位上的编码值的大小
        4. 成员运算符：
            判断某个值或元素是否存在于序列中, 存在返回True；否则返回False
            对象 in 序列
            对象 not in 序列


"""

a = 'hello'
b = 'world'
print(a + b)
print(a * 3)

a += b
print(a)
b *= 4
print(b)

# 3. 比较运算符
print(ord('a'))  # 97
print(ord('b'))  # 98
print('a' == 'b')
print('a' > 'b')
print('a' < 'b')
print('aa' == 'ab')

# 4. 成员运算符
info = "welcome to China"
print('w' in info)
print('to' in info)
print('Come' in info)
print('Come' not in info)

```

### 索引 index

- 格式：字符串[整数]

- 作用：通过索引访问对应的字符

- 说明：

  - 正向索引：从头到尾，索引值从0开始，依次增大

  - 反向索引：从尾到头，索引值从-1开始，依次减小

    | 字符串'Python' | P    | y    | t    | h    | o    | n    |
    | -------------- | ---- | ---- | ---- | ---- | ---- | ---- |
    | 正向索引       | 0    | 1    | 2    | 3    | 4    | 5    |
    | 反向索引       | -6   | -5   | -4   | -3   | -2   | -1   |

  ```python
  """
      索引 index
          容器名[索引值]
              索引值要求为整数
  
          注意边界问题：
              IndexError: string index out of range
  """
  
  s = "Python"
  
  # 正向索引
  print(s[0])
  print(s[1])
  print(s[3])
  
  # 反向索引：
  print(s[-1])
  print(s[-3])
  
  # 注意：边界问题
  # print(s[6]) # IndexError: string index out of range
  
  # 通过索引进行遍历
  for item in range(6):
      print(s[item])
  
  # 扩展：获取容器长度
  # len()
  print(len(s))  # 6
  
  print('---------')
  for item in range(len(s)):
      print(s[item])
  
  ```

### 切片 slice

- 格式：字符串`[[start_index]: [stop_index][: step]]` 
  - `start_index`: 起始索引， 正向索引不设置默认为开始位置，反向索引不设置默认为末尾位置。
  - `stop_index`: 结束索引, 不包含结束点，正向索引不设置默认为最后位置，反向索引不设置默认开始位置。
  - `step`: 步长:  切片每次获取元素后移的方向和偏移量。不设置默认为1
    - 当步长为正数时，正向切片
    - 当步长为负数时，反向切片
- 作用：截取多个元素
- 返回值：字符串类型

```python
"""
    切片：
        截取连续或一定间隔的字符结果
    语法：
        容器名[[起始索引] : [终止索引] [:步长]]
"""
s = '12345'

# 起始索引为: 终止索引
print(s[:])  # '12345'
print(s[::2])  # '135'

print(s[::-1])  # '54321'
print(s[4::-2])  # '531'
print(s[4:1:-2])  # '53'

# 注意
print(s[1:1])  # '' 不能切 开始索引和结束索引位置相同,结果为空字符串
print(s[3:1])  # '' 不能切 默认为正向切片,结果为空字符串
print(s[-len(s):1:-1])  # '' 起始和终止顺序为正向 切片为反向

print(s[:len(s)])  # '12345'

```

### 常用方法

```python
"""
    字符串常用方法
    https://www.runoob.com/python3/python3-string.html
"""

# ''.isdigit() 判断字符串是否全为数字
print('123'.isdigit())
print('123a'.isdigit())

# ''.upper() 转大写
# ''.lower() 转小写
print('abAdefg'.upper())
print('aAcdEfg'.lower())

# ''.isalpha() 是否为全字母
print('123456abc'.isalpha())
print('123456'.isalpha())

# ''.isalnum() 字符串中至少有一个字符且所有字符都是字母和数字
print(''.isalnum())
print('abc_'.isalnum())
print('123456'.isalnum())

print('   123456  \n  '.lstrip())  # 去除左侧空格 left
print('   123456  \n  '.rstrip())  # 去除右侧空格 right
print('   123456  \n  '.strip())  # 去除两个空格  left + right
print('---')

# ''.replace(old, new, count) 替换
s = 'banana'
print(s.replace('a', 'A'))  # 默认全部替换
print(s.replace('a', 'A', 1))  # 从左至右替换一个
print(s.replace('B', 'A', 1))  # 字符不存在, 不替换
print(s.replace('a', 'A', 4))  # 后续无效

```

### 格式化

```python
"""
    格式化字符串
        格式： "格式化占位符" %(参数值, ...)

    占位符：
        %s: 字符串格式占位符 (传递任何类型均可)
        %d: 整型占位符
        %f: 浮点型占位符   %.nf  表示小数点保留n为小数
        %%: %
"""
name = input("请输入姓名：")
age = int(input("请输入年龄："))
score = float(input("请输入成绩："))

# print("姓名为：%s, 年龄为: %d, 成绩为：%f, 排名：10%%" %(name, age, score))
# print("姓名为：%s, 年龄为: %d, 成绩为：%.2f, 排名：10%%" %(name, age, score))
# print("姓名为：%s, 年龄为: %s, 成绩为：%s, 排名：10%%" %(name, age, score))

# ''.format()
# '{} {}'.format(变量名1, 变量名2)
print("姓名为：{}, 年龄为:{} , 成绩为：{}".format(name, age, score))

# ''.format() 简写
# f'{变量名1} {变量名2}'
print(f"姓名为：{name}, 年龄为:{age} , 成绩为：{score}")


```

## 列表

- 由一系列变量组成的可变序列容器 【预留空间】。
  - 列表是可以存储任意数据类型的可变容器。
  - 列表中的元素之间有先后关系。

### 创建列表

```python
"""
    列表 list：
        由一系列变量组成的可变序列容器
"""

# 1. 创建列表
#   -- 空列表
list_01 = []
list_02 = list()
print(list_01, type(list_01))
print(list_02, type(list_02))

#   -- 非空列表
name = "唐三藏"
list_03 = [name, "空空", "八戒", "净净", 18, 19.5, True, 3j]
print(list_03, type(list_03))

# 参数必须为可迭代对象
list_04 = list("人工智能")
print(list_04, type(list_04))

list_05 = list(range(10))
print(list_05)
```

### 定位元素

```python
# 2. 定位元素
list_06 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#   -- 定位单个元素 --> 索引  --> 容器名[索引值]
print('索引为0的元素:', list_06[0])
print('索引为1的元素:', list_06[1])
print('索引为-1的元素:', list_06[-1])
print('索引为-5的元素:', list_06[-5])
# IndexError: list index out of range
# print('索引为-5的元素:', list_06[11]) # 索引超出范围

#   -- 定位多个元素 --> 切片  --> 容器名[起始索引:终止索引:步长]
print(list_06[:])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(list_06[1:])  # ['B', 'C', 'D', 'E', 'F', 'G']
print(list_06[1:5])  # ['B', 'C', 'D', 'E']
print(list_06[1:5:2])  # ['B', 'D']
print(list_06[-1:-5:-2])  # ['G', 'E']
```

### 修改元素

```python
"""
    列表操作：

"""
list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 修改操作
#   -- 单个元素修改 --> 列表名[索引]= 值
list_01[-1] = 'JavaScript'
print(list_01)

#   -- 多个元素修改 --> 列表名[起始:结束:步长] = 可迭代对象
list_01[::2] = [1, 2, 3]
print(list_01)

# 切片元素个数 < 值的个数, 产生 ValueError
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3
list_01[::2] = "abc"
print(list_01)

```

### 删除元素

```python
"""
    列表
        增加元素
            指定位置插入元素：
            尾部追加：
        删除元素
"""
list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 增加元素
#   -- 指定位置插入元素  列表名.insert(index, value)
list_01.insert(0, 'AID')

print(list_01)  # ['AID', 'Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']
list_01.insert(1, 'tedu')
print(list_01)

#  -- 末尾追加  列表名.append(value)
list_01.append("Numpy")
print(list_01)

# 删除元素
#   -- 删除指定索引的元素
#       列表名.pop(index=-1) 默认为-1 删除最后一个元素
#       返回值为：删除的元素
list_01.pop()
print(list_01)

list_01.pop(1)
print(list_01)

# list_01.pop(100) # IndexError: pop index out of range
# print(list_01)

#   -- 删除指定元素
#       列表名.remove(元素)
#       删除元素不存在，则出发ValueError异常
list_01.remove('PHP')
print(list_01)
# list_01.remove('ABC')

```

### 遍历列表

```python
"""
    列表：
        遍历：
            正向遍历：
                for 变量 in 非空列表:
                    循环体

                for 索引值 in range(len(非空列表)):
                    循环体

            反向遍历：
                for 索引值 in range(len(非空列表)-1, -1, -1):
                    循环体
"""

list_01 = ['Python', 'Java', 'C', 'C++', 'MySQL', 'PHP']

# 1. 正向遍历
# for 变量 in 非空列表:
#     循环体

for i in list_01:
    print(i)

# for 索引值 in range(len(非空列表)):
#     循环体
for index in range(len(list_01)):
    print(list_01[index])

print('-' * 50)

# 2. 反向遍历
# for 索引值 in range(len(非空列表)-1, -1, -1):
#     循环体
for index in range(len(list_01) - 1, -1, -1):
    print(list_01[index])

```

### 内置函数

```python
"""
    列表内置函数
        max() 返回容器中最大的元素
        min() 返回容器中最小的元素
        sum() 返回容器中元素的和
        len() 返回容器的长度
"""
list_01 = [1, 3, 5, 7]

print('和为：', sum(list_01))
print('最大为：', max(list_01))
print('最小为：', min(list_01))
print('长度为：', len(list_01))

```

```python
"""
    循环录入学生的成绩, 如果输入为空, 则结束输入
    1. 打印所有学生的成绩
    2. 打印共有多少学生的成绩
    3. 打印最高分、最低分和平均分数
"""
```























