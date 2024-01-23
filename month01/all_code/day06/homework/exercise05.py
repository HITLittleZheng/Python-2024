"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
"""
list_regions = []
while True:
    region = input("请输入疫情地区名称：")
    # if region == "":
    if not region:
        break
    if region in list_regions:
        print("已经存在")
    else:
        list_regions.append(region)

# len(list_regions) - 1:从总数-1的位置开始
# -1：不包含-1,实际包含0(第一个位置)
# -1：倒序
for i in range(len(list_regions) - 1, -1, -1):
    print(list_regions[i])


# list01 = ["a","b","c"]

# for i in range(len(list01) - 1, -1, -1):
#     print(list01[i])
#
# for item in list01[len(list01) - 1: -1: -1]:
#     print(item)



