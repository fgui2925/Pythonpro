import random

random_lst=[]
for i in range(10):
    random_lst.append(random.randint(1,100))
print(random_lst)
# random_lst2=[random.randint(1,100) for i in range(10)] # 使用列表生成式生成列表

def max_num(lst):
    num=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>num:
            num=lst[i]
    return num

print(max_num(random_lst))