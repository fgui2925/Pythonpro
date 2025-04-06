birth_year=[88,89,90,98,00,99]
print(birth_year)

# 方法1
for i in range(0,len(birth_year)):
    if birth_year[i]!=0:
        birth_year[i]+=1900
        birth_year[i]=str(birth_year[i])
    else:
        birth_year[i]+=2000
        birth_year[i] = str(birth_year[i])
print(birth_year)

print('-'*40)

# 方法2
birth_year=[88,89,90,98,00,99]
print(birth_year)
for i in range(0,len(birth_year)):
    if str(birth_year[i])!='0':
        birth_year[i]='19'+str(birth_year[i])
    else:
        birth_year[i]='200'+str(birth_year[i])
print(birth_year)

print('-'*40)

# 方法3
birth_year=[88,89,90,98,00,99]
print(birth_year)
for index,value in enumerate(birth_year):
    if str(value)!='0':
        birth_year[index]='19'+str(value)
    else:
        birth_year[index] = '200' + str(value)
print(birth_year)