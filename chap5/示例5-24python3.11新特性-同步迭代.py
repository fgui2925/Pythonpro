fruits = {'apple', 'banana', 'orange', 'strawberry'}  #集合是无序的，每次运行结果各不相同。若要全部匹配上可以换成列表或元组
counts = {10,3,4,5}  #集合是无序的，，每次运行结果各不相同。若要全部匹配上可以换成列表或元组
for f,c in zip(fruits, counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'banana',3:
            print('3个香蕉')
        case 'orange',4:
            print('4个橘子')
        case 'strawberry',5:
            print('5个草莓')
        case _:
            print('未找到！')