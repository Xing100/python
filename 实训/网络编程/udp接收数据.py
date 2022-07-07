from socket import *


# 创建套接字
udp = socket(AF_INET,SOCK_DGRAM)
local_addr = ("",8080)
# 绑定端口
udp.bind(local_addr)  # bind里面放的是元祖
# 等待接收对方的数据
recv_data = udp.recvfrom(1024)  # 1024表示本次接收的最大字节
# 返回的recv_data是一个元祖r,ecv_data[0]放的是接收的数据,ecv_data[0]返回的是ip地址和端口号

# 显示接收到的数据
print(recv_data[0].decode("utf-8"))  # ecv_data[0]需要编码   ecv_data[1]不需要编码
# 关闭套接字
udp.close()
