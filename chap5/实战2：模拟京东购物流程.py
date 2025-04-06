varehouse=dict()
for i in range(5):
    d=input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
    k=d[0:4:1]
    v=d[4::1]
    varehouse[k]=v
for k,v in varehouse.items():
    print(k,v)

shoppingcart=list()
j=''
while j!='q':
    key=input('请输入要购买的商品编号：')
    j=key
    if j=='q':
        break
    elif varehouse.get(key):
        shoppingcart.append(key+varehouse.get(key))
        print('商品成功添加到购物车！')
    else:
        print('商品不存在！')
print('-'*40)
# shoppingcart.sort(reverse=True) # 按字符串对应的ASCII码表值，降序排序
shoppingcart.reverse()    # 按列表索引降序排序
for item in shoppingcart:
    print(item)

