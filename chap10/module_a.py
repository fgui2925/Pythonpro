# print('welcome to beijing')
# name='ysj'
# print(name)

# 主程序运行：阻止了全局变量的数据被输出执行。
# 导入到其他模块时，不希望这部分代码被执行时，使用主程序运行
if __name__ == '__main__':
    print('welcome to beijing')
    name='ysj'
    print(name)