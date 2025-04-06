import json
# 准备高维数据
lst=[
    {'name':'张三','age':18,'score':90},
    {'name':'李四','age':21,'score':99},
    {'name':'王五','age':19,'score':89}
]
# 使用.dumps将数据转为json格式
s=json.dumps(lst,ensure_ascii=False,indent=4) #ensure_ascii正常显示中文，indent增加数据的缩进，美观用，使json字符串更具有可读性
print(type(s)) # json.dumps是编码的过程 lst--->str，列表中是列表
print(s)

# 使用.loads进行解码
lst2=json.loads(s)
print(type(lst2))
print(lst2)

# 使用.dump将数据转为json格式并编码到文件中
with open('student.txt','w',encoding='utf-8') as file:
    json.dump(lst2,file,ensure_ascii=False,indent=4)

# 使用.load从文件中解码到程序
with open('student.txt','r',encoding='utf-8') as file:
    lst3=json.load(file) # 直接是列表类型
    print(type(lst3))
    print(lst3)