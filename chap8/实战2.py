def get_num(s):
    lst=[]
    s_sum=0
    for i in range(len(s)):
        if s[i].isdigit():
            lst.append(int(s[i]))
            s_sum+=int(s[i])
    return lst,s_sum

x=input('请输入一个字符串:')
a,b=get_num(x)  # 系列解包赋值
print('提取的数字列表为:',a)
print('累加和为:',b)