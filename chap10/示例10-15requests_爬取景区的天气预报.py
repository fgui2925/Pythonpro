import requests
import re
url='https://www.weather.com.cn/weather1d/101010100.shtml' # 爬虫打开的浏览器上的网页
resp=requests.get(url) #打开浏览器并打开网址
# 设置一下编码格式（显示中文需要）
resp.encoding='utf-8'
print(resp.text) # resp是响应对象，使用对象名.属性名进行调用

'''
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">27/18℃</span>
<span class="zs">适宜</span>
'''

city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
print(city)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
print(weather)
# wd=re.findall('<span class="wd">(\\w*/\\w*℃)</span>',resp.text)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
print(wd)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)
print(zs)

lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
print(lst)
for item in lst:
    print(item)