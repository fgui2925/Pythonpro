number=eval(input('请输入一个4位整数：'))
print('个位上的数为：',number%10)
print('十位上的数为：',number//10%10)
print('百位上的数为：',number//100%10)
print('千位上的数为：',number//1000)

num2=input('请输入一个4位整数：')
print('个位上的数为：',num2[3])
print('十位上的数为：',num2[2])
print('百位上的数为：',num2[1])
print('千位上的数为：',num2[0])