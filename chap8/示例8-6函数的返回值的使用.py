# 函数的返回值
def calc(a,b):
    print(a+b)
#调用
calc(10,20)
print(calc(1,2)) #None
print('-'*50)

def calc2(a,b):
    s=a+b
    return s
# 调用方式1：存储到变量中
get_s=calc2(1,2)
print(get_s)
# 调用方式2：直接参与下一次的运算
get_s2=calc2(calc2(1,2),3)
print(get_s2)

# 返回值可以是多个
def get_sum(num):
    s=0 # 存储累加和
    odd_sum=0 # 存储奇数和
    even_sum=0 # 存储偶数和
    for i in range(1,num+1):
        s+=i
        if i%2==0:
            odd_sum+=i
        else:
            even_sum+=i
    return s,odd_sum,even_sum # 3个返回值

result=get_sum(10)
print(type(result))  # <class 'tuple'>
print(result)

# 系列解包赋值
a,b,c=get_sum(10)
print(a)
print(b)
print(c)
