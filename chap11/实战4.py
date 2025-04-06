
def add_reply(s):
    with open('reply.txt','a',encoding='utf-8') as f:
        f.write(s)
        f.write('\n')

def show_reply():
    with open('reply.txt','r',encoding='utf-8') as f:
        for item in f.readlines():
            print(item,end='')

def load_reply(qs):
    with open('reply.txt','r',encoding='utf-8') as f:
        for item in f.readlines():
            key_word=item.split('|')[0]
            if key_word in qs:
                return item
                break
        return False

if __name__ == '__main__':
    # s1='订单|如果您有任何订单问题，可以登录沟宝账号。点击“我的订单”，查看订单详情'
    # s2='物流|如果你有任何物流问题，可以登录淘宝账号。点击“我的订单”，查看商品物流'
    # s3='账户|如果您有任何账户同照，可以联系淘宝客服。电话:XXxX-XXXXXX'
    # s4='支付|如果您有任何支付问题，可以联系文付宝客服。QQ:xxxxxxx'
    # add_reply(s1)
    # add_reply(s2)
    # add_reply(s3)
    # add_reply(s4)
    # show_reply()
    question = input('HI,xxx你好,小蜜在此等主人很久了，有什么烦恼快和小蜜说说吧~')
    while True:
        if question=='bye':
            break
        else:
            result=load_reply(question)
            if result:
                print(result)
                question = input('您还可以问我一些关于订单，物流，支付等问题，退出请输入bye')
            else:
                question = input('小蜜不知道您说的是什么，您可以问一问关于订单，物流，支付等问题，退出请输入bye')
    print('小主再见')