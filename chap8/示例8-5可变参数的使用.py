# 个数可变的位置参数
def fun (*para):
    print(type(para))
    for item in para:
        print(item)
# 调用
fun(10,20,30,40)
fun(10)
fun([11,22,33,44]) #把整个列表作为一个元素传到元组中，实际上传递的是一个参数
# 在调用时，参数前加一颗*，会将列表进行解包
fun(*[11,22,33,44])
print('-'*50)

# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key, '--->',value)
#调用
fun2(name='张三',age=18,height=170)

d={'name':'张三','age':18,'height':170}
# fun2(d) # TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)  # 在调用时，字典前加两颗*，会进行系列解包操作
