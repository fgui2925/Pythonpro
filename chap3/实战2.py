father=eval(input('请输入父亲的身高：'))
mother=eval(input('请输入母亲的身高：'))
print('预测儿子的身高为：',round((father+mother)*0.54,2)) #round(value，2)保留2位小数

father=input('请输入父亲的身高：')
mother=input('请输入母亲的身高：')
print('预测儿子的身高为：',(float(father)+float(mother))*0.54)