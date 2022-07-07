import requests
url = 'https://www.iqiyi.com/'

requests.get(url)

r = requests.get(url) #r是返回的Response
print(r.text)
print(r.status_code) #响应码
print(r.encoding) #编码方式
print(r.apparent_encoding)  #备用编码方式
r.encoding = 'utf-8'
print(r.text)



