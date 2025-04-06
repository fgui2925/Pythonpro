import pdfplumber
# 打开pdf文件
with pdfplumber.open('小学数学-公式.pdf') as pdf:
    for page in pdf.pages: # 遍历页，这个page不是1/2/3，而是是一个页码对象
        print(page.extract_text()) # extract_text()方法提取内容
        print(f'---------第{page.page_number}页结束-------------')
