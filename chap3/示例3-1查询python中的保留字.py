import keyword # 导入keyword关键字的内置模块（内置模块即安装python解释器的时候直接跟解释器一起安装过来的）
print('保留字清单：',keyword.kwlist) # 输出保留字清单
#注意：保留字是严格区分大小写的。
print('保留字个数：',len(keyword.kwlist)) # 获取保留字的个数