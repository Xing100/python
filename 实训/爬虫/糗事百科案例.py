import requests
import re

url = "http://www.qiushibaike.com/text/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

response = requests.get(url,headers=header)
info = response.text
# print(info)
infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)
# print(infos)
with open("段子.txt", "w", encoding="utf-8")as f:
    for i in infos:
        f.write(i+"\n\n\n")
