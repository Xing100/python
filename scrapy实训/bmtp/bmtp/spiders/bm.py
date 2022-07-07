import scrapy
from bmtp.items import BmtpItem

class BmSpider(scrapy.Spider):
    name = 'bm'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series-t/3302.html']

    def parse(self, response):
        titles = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/a[1]/text()").getall()
        for title in titles:
            # print(title)
            urls = response.xpath("//ul/li/a/img/@src").getall()    #img/@src 只提取img标签中的src属性     缺少http:
            # for url in urls:
            #     url = response.urljoin(url)     #urljoin   自动拼接url
            #     print(url)
            urls = list(map(lambda src:response.urljoin(src),urls))     #拼接url
            # print(urls)
            # itme = BmtpItem(title=title, urls=urls)
            itme = BmtpItem(title=title,urls=urls)
            yield itme


