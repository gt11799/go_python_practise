# coding: utf-8
# 求字符串的子集
# 123 -> 1，2，3，12，13，23，123，子集的个数，字符串里没有重复的字符
# 12345 1 23 13 34 135
# 1 2 3 4 5 
# 12 23 25
# 12345 13452

result = set([])
    
# def get_all_sub_set(string):
#     def _get_all_sub_set(left_string, string):
#         new_left_string = left_string + string[0]
#         if len(string) == 1:
#             result.append(new_left_string)
#             return
#         result.append(new_left_string)
#         _get_all_sub_set(new_left_string, string[1:])
#     for idx in range(len(string)):
#         _get_all_sub_set("", string[idx:])


def get_all_string(tmp_list):
    result_list = []
    def _get_all_string(tmp_list):
        if len(tmp_list) == 1:
            return
        left = tmp_list[0]
        for char in tmp_list[1:]:
            result_list.append(left + char)
        _get_all_string(tmp_list[1:])
    _get_all_string(tmp_list)
    return result_list
        

def get_all_sub_set(string):
    for char in string:
        result.add(char)
    def _get_sub_set(string, result_length):
        pass
    return


print(get_all_string(["1", "2", "3", "4"]))
# get_all_sub_set("12345")
print result, len(result)
