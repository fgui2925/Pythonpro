import re

# sub函数，查找字符串中所有符合pattern的内容，并将查找到的内容替换成自定义的内容
# split函数，根据字符串中符合pattern的分隔符，将字符串内容进行分割，结果是一个列表
pattern ='黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://www.baidu.com/s?wd=python&rsv_spt=1'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)