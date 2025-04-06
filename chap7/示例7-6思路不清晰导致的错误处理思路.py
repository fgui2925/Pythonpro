lst=[
    {'rating':[9.7,50],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['帶姆.罗宾斯','摩根.弗里曼']},
    {'rating':[9.6,50],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
    {'rating':[9.6,50],'id':'1296141','type':['剧情','犯罪’"怂疑'],'title':'控方证人','actors':['桼隆.鲍华','玛琳.黛德丽']},
]

name=input('请输入你要查询的演员:')
for item in lst:
    # for movie in item:
    #     actors=movie['actors']
    #     if name in actors:
    #         print(name,'出演了',movie)
    # print(item)
    # print(item.get('actors'))
    if name in item.get('actors'):
        # print(item['title'])
        print(name,'出演了',item['title'])