lst=[
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400]
]
print('编号\t\t名称\t\t\t品牌\t\t单价'),
for i in lst:
    for j in i:
        print(j,end='\t\t')
    print()

# 格式化操作
for i in lst:
    i[0]='0000'+i[0]
    i[3]='￥{0:.2f}'.format(i[3])

print('编号\t\t\t名称\t\t\t品牌\t\t单价'),
for i in lst:
    for j in i:
        print(j, end='\t\t')
    print()
