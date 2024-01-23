"""

"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}
# 打印于谦的所有爱好(一行一个)
for item in dict_hobbies["于谦"]:
    print(item)

# value = dict_hobbies["于谦"]
# for i in range(len( value )):
#     if len(value[i]) ==2:
#         value[i] = ""
# print(dict_hobbies)

# 　计算郭德纲所有爱好数量
print(len(dict_hobbies["郭德纲"]))

# 打印所有人(一行一个)
for key in dict_hobbies:
    print(key)

# 打印所有爱好(一行一个)
for value in dict_hobbies.values():
    for item in value:
        print(item)

# ---------
dict_hobbies["于谦"].remove("抽烟")
dict_hobbies["郭德纲"][-1] = "演"

dict_hobbies["大爷"] = dict_hobbies["于谦"]
del dict_hobbies["于谦"]

print(dict_hobbies)