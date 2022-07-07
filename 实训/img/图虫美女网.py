from selenium import webdriver
import requests
import parsel    #解析数据
from urllib.parse import urlencode   #用来转码
from fake_useragent import UserAgent
from time import sleep



opetions = webdriver.ChromeOptions()
opetions.add_argument('--headless')
opetions.add_argument('--disable-gpu')
gg = webdriver.Chrome(chrome_options=opetions)   #设置无头浏览器

def seleniumgeturl(url):     #获取主页
    gg.get(url)
    html = gg.page_source
    return html


def requestsget(url):     #获取图片
    headers = {"User-Agent": UserAgent().random,
               "cookie": "lang=zh; _ga=GA1.2.650175262.1613713777; weilisessionid3=c00c2fd831236fea9140467966e0d8a9; wluuid=WLGEUST-DEAEDF80-2307-D524-3516-F382AC6E3090; ssoflag=0; _ga=GA1.3.650175262.1613713777; wluserid=2451522; wlnickname=%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83; wlsource=extbaidupz1; utm_term=sem_baidu_pz_duocai_tuchong01; _gid=GA1.3.607763984.1615466237; accessId=e7dfc0b0-b3b6-11e7-b58e-df773034efe4; Hm_lvt_f212e14a5ffb8199fd0e64061c054314=1615646545,1615688910,1615689162,1615697390; qimo_seosource_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=%E7%99%BE%E5%BA%A6%E6%90%9C%E7%B4%A2; qimo_seokeywords_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=%25E5%259B%25BE%25E8%2599%25AB%25E7%25BD%2591; qimo_xstKeywords_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=; href=https%3A%2F%2Fstock.tuchong.com%2F%3Fsource%3Dextbaidupz1%26utm_source%3Dextbaidupz1%26utm_term%3Dsem_baidu_pz_duocai_tuchong01; webp_enabled=1; Hm_lpvt_f212e14a5ffb8199fd0e64061c054314=1615697549; pageViewNum=156"
               }
    # sleep(3)
    response = requests.get(url,headers = headers,)
    byte = response.content
    if response.status_code == 200:
        return byte
    else:
        return None


def parselurl(html):
    x = parsel.Selector(html)
    urls = x.xpath("//img/@data-src").getall()
    return urls

# def updateurl(url):
#     url = "https:"+url
#     url = url.replace("sm","l")
#     return url



def savebyte(byte,imgname):
    with open(imgname,"wb")as f:
        f.write(byte)


def main():
    base_url = "https://stock.tuchong.com/search?{}"
    lx = input("请输入要爬取的类型:")
    pns = int(input("请输入要爬取多少页:"))
    print("是否选择vip")
    xuanze = input("是或否:")
    if xuanze == "是":
        platform = "weili_vip"
    else:
        platform = ""
    for pn in range(pns):
        pn += 1
        print(pn)   #查看第几页
        args = {
            "term":lx,
            "page":pn,
            "platform":platform
        }
        args = urlencode(args)   #转码
        print(base_url.format(args))   #查看页数url
        html = seleniumgeturl(base_url.format(args))
        urls = parselurl(html)

        urls = ["https:"+url.replace("sm","l") for url in urls]     #列表推导式写法   #更新urls

        # upurls = []     #函数写法    #更新urls
        # for url in urls:
        #     url = updateurl(url)
        #     print(url)     #显示url
        #     upurls.append(url)

        # urls = list(map(lambda url:"https:"+url.replace("sm","l"),urls ))    #匿名函数写法    #更新urls
        # for url in urls:
        #     print(url)
        t = 0

        for url in urls:
            print(url)   #显示url
            imgname = url[url.rfind("/")+1:-5]+".jpg"    #显示图片名称
            # print(imgname)
            byte = requestsget(url)
            if byte != None:
                savebyte(byte,imgname)
            else:
                print("错误")
            # t += 1
            # if t % 5 == 0:
            #     sleep(5)





if __name__ == '__main__':
    main()
