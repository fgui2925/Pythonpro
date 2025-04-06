fp=open('note1.txt','w') # 打开文件
print('人生苦短，我用python。',file=fp) # 输出内容到文件中
fp.close() # 关闭文件