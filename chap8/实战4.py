# lst=['hello','world','python']
# def in_lst(s):
#     for item in lst:
#         if item==s:
#             result='存在'
#             break
#         else:
#             result='不存在'
#     return result
#
# x=input('请输入您要判断的字符串:')
# print(in_lst(x))

def get_find(s,lst):
    for item in lst:
        if item==s:
            return True
    return False
lst1=['hello','world','python']
x=input('请输入您要判断的字符串:')
result=get_find(x,lst1)
print('存在' if result else '不存在')