from socket import *


# 创建套接字
udp = socket(AF_INET,SOCK_DGRAM)
# 要发送的目的主机
dest_addr=('192.168.216.1',8080)
# 要发送的数据
send_data = input("请输入要发送的数据:")
# 编码
udp.sendto(send_data.encode("utf-8"),dest_addr)
# 关闭套接字
udp.close()