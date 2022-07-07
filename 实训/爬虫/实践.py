import requests
import parsel
from selenium import webdriver
import csv


opetions = webdriver.ChromeOptions()
opetions.add_argument('--headless')
opetions.add_argument('--disable-gpu')
gg = webdriver.Chrome(chrome_options=opetions)   #设置无头浏览器

def seleniumgeturl(url):     #获取主页
    gg.get(url)
    html = gg.page_source
    return html

def requestsgethtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Cookie": "guid=e337320471c799839e2e7e46e7903ff1; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26rec"
                  "entSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26rece"
                  "ntSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60120000%7C%21ord_field%7E%600%7C"
                  "%21recentSearch0%7E%60120000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99"
                  "%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA"
                  "99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21"
    }
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    html = response.text
    return html


def parselurl(html):
    x = parsel.Selector(html)
    urls = x.xpath("//div[@class='j_joblist']/div[@class='e']/a/@href").getall()
    return urls


def parselhtml(html):
    x = parsel.Selector(html)
    title = x.xpath("//div/h1/@title").get()
    gongsi = x.xpath("//p/a/@title").get()
    gongzi = x.xpath("//div [@class='cn']/strong/text()").get()
    zhiwei = x.xpath("//div[@class='com_tag']/p/a/text()").get()
    info = str(title)+"  "+str(gongsi)+"  "+str(gongzi)+"  "+str(zhiwei)
    return info


def saveinfo(info):
    with open("工作信息.txt", "a", encoding="utf-8")as f:
        f.write(info+"\n")





def main():
    base_url = "https://search.51job.com/list/120000,000000,0000,00,9,99,+,2,{}"
    pn = int(input("请输入要抓取多少页:"))
    for i in range(1,pn+1):
        a = str(i)+".html"
        url = base_url.format(a)
        print(url)
        html = seleniumgeturl(url)
        urls = parselurl(html)
        print(urls)
        for url in urls:
            html = requestsgethtml(url)
            info = parselhtml(html)
            saveinfo(info)



if __name__ == '__main__':
    main()