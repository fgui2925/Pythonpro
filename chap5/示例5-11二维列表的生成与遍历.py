# 二维列表的生成
lst=[
    ['城市','同比','环比'],
    ['北京',102,103],
    ['上海','104','504'],
    ['深圳','100','39']
]
print(lst)

# 遍历二维列表使用双层for循环
for row in lst:
    for item in row:
        print(item,end=' ')
    print()

# 列表生成式生成一个4行5列的二维列表
lst2=[[j for j in range(5)] for _ in range(4)]
print(lst2)