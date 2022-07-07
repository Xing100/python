
import requests


url = "http://icweiliimg1.pstatp.com/weili/sm/852203511054598156.webp"
info = requests.get(url)
info = info.content
with open("f.jpg","wb")as f:
    f.write(info)


