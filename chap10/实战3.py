import jieba
from wordcloud import WordCloud

# 把文件读取进来
with open('小学数学-公式.txt','r',encoding='utf-8') as file:
    s=file.read()

# 分词
lst=jieba.lcut(s)

# 排除词
stopword=['0','公式','高']

txt=''.join(lst)
# 绘制词云图
wordcloud=WordCloud(background_color='white',font_path='msyh.ttc',stopwords=stopword,width=800,height=400)

# 由txt生成词云图
wordcloud.generate(txt)
# 保存图片
wordcloud.to_file('wordcloud.png')
