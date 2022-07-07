from urllib.request import urlopen
from urllib.request import Request
#from urllib.parse import quote
#from urllib.parse import urlencode
url = "https://www.baidu.com/s?wd=%E5%B0%9A%E5%AD%A6%E5%A0%82"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}   #伪装浏览器请求头
request = Request(url,headers=headers)   #创建request对象
response = urlopen(request)  #抓包
info = response.read()   #读内容
print(info.decode())   #转码
with open ("dfd.html","wb")as f:
    f.write(info)




'''
from urllib.parse import quote
from urllib.parse import urlencode
args = {
    "wd":"尚学堂" 
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))
print(quote("尚学堂"))
解码
'''
