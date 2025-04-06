score=eval(input('请输入您的成绩：'))
# 多分支结构 if...elif...else
if score<0 or score>100:
    print('您输入的成绩有误！')
elif score<60:
    print('E')
elif score<70:
    print('D')
elif score<80:
    print('C')
elif score<90:
    print('B')
else:
    print('A')