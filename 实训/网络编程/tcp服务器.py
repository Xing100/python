from socket import *
import re
import  multiprocessing



def serveice_client(new_socket):
    """为这个客户端返回数据"""

    #  接收浏览器发来的请求，即http服务
    #  GET / HTTP1.1
    recv_data = new_socket.recv(1024)
    print(recv_data)
    # 返回的内容
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    f = open("f.html", "rb")
    html = f.read()
    f.close()
    #  回送数据
    new_socket.send(response.encode("gbk"))  # 利用新的套接字服务客户
    new_socket.send(html)
    #  关闭套接字
    new_socket.close()

def main():
    #创建套接字
    tcp = socket(AF_INET,SOCK_STREAM)
    # 绑定本地ip端口
    local_addr = ("",8080)
    tcp.bind(local_addr)
    # 监听
    tcp.listen(128)
    while True:
        # 等待请求
        new_socket,client_addr = tcp.accept()  #new_socket创建新的套接字，client_addr返回对方ip和端口号
        print(client_addr)  #对方ip端口号
        serveice_client(new_socket)

    tcp.close()

if __name__ == '__main__':
    main()