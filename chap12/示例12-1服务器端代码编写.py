from socket import socket,AF_INET,SOCK_STREAM
# AF_INET 表示用于Internet之间的进程通信。
# SOCKET_STREAM 表示的是用TCP协议编程

# (1)创建socket对象
sever_socket=socket(AF_INET,SOCK_STREAM)

# (2)绑定IP地址和端口
ip='127.0.0.1' #192.168.168.2
port=8888
sever_socket.bind((ip,port))

# (3)开始TCP监听
sever_socket.listen(5)
print('服务器已启动')

# (4)等待客户端的连接
client_socket,client_addr=sever_socket.accept() #系列解包赋值

# (5)接收客户端的数据,定义可接收的数据长度
data=client_socket.recv(1024)
print('客户端发送过来的数据为',data.decode('utf-8'))

# (6)关闭
sever_socket.close()