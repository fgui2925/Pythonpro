s=set()
for i in range(1,6):
    info=input('请输入第'+str(i)+'位好友的姓名与手机号码:')
    s.add(info)

for item in s:
    print(item)