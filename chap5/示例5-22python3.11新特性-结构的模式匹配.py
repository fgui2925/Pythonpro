data=eval(input('请输入需要匹配的数据：'))
match data:
    case {'name':'张三','age':20}:
        print('字典')
    case [10,20,30]:
        print('列表')
    case (10,20,30):
        print('元组')
    case _:  #等同于if...else中的else
        print('不是字典、列表、元组')
