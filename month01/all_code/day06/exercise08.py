"""
# 练习：在终端中循环录入多个省份名称,
#      如果输入空字符串则停止。
#      最后打印每个省份名称
# 要求：省份不能重复.
"""
set_regions = set()
while True:
    region = input("请输入省份名称：")
    if region == "":
        break
    set_regions.add(region)

print(set_regions )
