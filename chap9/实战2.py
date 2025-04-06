class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def info(self):
        print(self.name,self.age,self.gender,self.score)

print('请输入5位学生信息：姓名#年龄#性别#成绩')
lst=[]
for i in range(1,6):
    x=input(f'请输入第{i}位学生信息及成绩:')
    s=x.split('#')
    stu=Student(s[0],s[1],s[2],s[3])
    lst.append(stu)

for item in lst:
    item.info()


