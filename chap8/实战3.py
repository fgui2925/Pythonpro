def trans_s(s):
    s_new=''
    for item in s:
        if item==item.upper():  # 也可以写成 'A'<=item<='Z'
            s_new+=item.lower()
        elif item==item.lower(): # 也可以写成 'a'<=item<='z'
            s_new+=item.upper()
        else:
            s_new+=item
    return s_new

x=input('请输入一个字符串:')
print(trans_s(x))