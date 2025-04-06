s='伟大的中国梦'
# 编码 str-->bytes
scode=s.encode(errors='replace' ) #默认是utf-8，因为utf-8中，英文占一个字节，中文占3个字节
print(scode)

scode_gbk=s.encode(encoding='gbk',errors='replace') # gbk中中文占2个字节
print(scode_gbk)

# 编码中的出错问题
s2='耶✌'
s2code=s2.encode(encoding='gbk',errors='ignore') # 编码出错时忽略
print(s2code)
s2code = s2.encode(encoding='gbk', errors='replace') #编码出错时，用?替代
print(s2code)
# s2code=s2.encode(encoding='gbk',errors='strict') #编码出错时报错 UnicodeEncodeError
# print(s2code)

# 解码过程bytes-->string
print(bytes.decode(scode_gbk,encoding='gbk')) #用gbk编码，就要用gbk解码
print(bytes.decode(scode,encoding='utf-8')) #用utf-8编码，就要用utf-8解码