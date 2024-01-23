"""
    字典推导式
"""
# key:range(10)
# value:key ** 2

# dict_result = {}
# for number in range(10):
#     dict_result[number] = number ** 2
# print(dict_result)
dict_result = {number: number ** 2 for number in range(10)}
print(dict_result)

dict_result = {number: number ** 2 for number in range(10) if number % 2 == 0}
print(dict_result)
