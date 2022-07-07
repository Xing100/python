import requests
import re
from fake_useragent import UserAgent


url = "https://tuchong.com/2610235/19654479/"
headers={"User-Agent":UserAgent().random}
response = requests.get(url,headers=headers)
html = response.text
all_url = re.findall(r'<img.id=.*src="(.*)".alt',html)
print(all_url)
for url in all_url:
    headers = {"User-Agent": UserAgent().random}
    response = requests.get(url, headers=headers)
    data = response.content
    filename = url[url.rfind("/")+1:]    #切片
    with open(filename,"wb")as f:
        f.write(data)
