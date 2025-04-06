number=eval(input('请输入您的6位兑奖号码：'))
# if...else
if number==987654:
    print("恭喜您中奖了！")
else:
    print("很遗憾您未中奖。")

#-------以上代码可以使用条件表达式进行简化-----

result='恭喜您中奖了！' if number==987654 else '很遗憾您未中奖。' # 判断结果为True，执行if之前的赋值，判断结果为False，执行else之后的赋值。
print(result)

print('恭喜您中奖了！' if number==987654 else '很遗憾您未中奖。') # 判断结果为True，执行if之前的输出，判断结果为False，执行else之后的输出。
