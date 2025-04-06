from socket import socket,AF_INET,SOCK_DGRAM
# (1)创建对象
send_socket = socket(AF_INET,SOCK_DGRAM)

while True:
    # (2)准备发送的数据
    data = input('请输入要咨询的问题:')
    # (3)设置接收方的IP和端口
    ip_port = ('127.0.0.1', 8888)
    # (4)发送数据
    send_socket.sendto(data.encode('utf-8'),ip_port)
    if data == 'bye':
        break
    # (5)准备接收接收方的回复
    recv_data,addr=send_socket.recvfrom(1024)
    info=recv_data.decode('utf-8')
    print(f'客服说:{info}')

# (6)关闭
send_socket.close()