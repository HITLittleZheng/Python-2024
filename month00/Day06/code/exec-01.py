"""
    计算一段字符串中出现过的字符及出现过的次数.
    输入：'abcdefgabcdabcab'
    输出：
        a --> 4次
        b --> 4次
        c --> 3次
        d --> 2次
        e --> 1次
        f --> 1次
        g --> 1次

"""
s = input("请输入: ")

chars = []  # 用来存储出现的字符
times = []  # 用来存储 chars 中字符出现的次数

for ch in s:
    if ch not in chars:
        chars.append(ch)
        times.append(1)
    else:
        # 已经存在于 chars 中
        index = chars.index(ch)  # 得到索引值
        times[index] += 1

for i in range(len(chars)):
    print(f"{chars[i]} 出现了 {times[i]} 次")
