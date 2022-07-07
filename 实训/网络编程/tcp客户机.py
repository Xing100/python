from socket import *


tcp = socket(AF_INET,SOCK_STREAM)
# 目的信息
sever_ip = input("请输入服务器的ip地址:")
sever_port = int(input("请输入服务器的端口号:"))
# 链接服务器
tcp.connect((sever_ip,sever_port))  # connect参数放元祖
# 发送的数据
send_data =input("请输入要发送的数据:")
tcp.send(send_data.encode("gbk"))

# 接收对方发送来的数据，最大字节不超过1024
recvData = tcp.recv(1024)
print("接收的数据为:",recvData.decode("gbk"))

# 关闭套接字
tcp.close()


