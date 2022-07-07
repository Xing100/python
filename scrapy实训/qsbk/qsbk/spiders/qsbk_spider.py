import scrapy
from qsbk.items import QsbkItem       #利用items传递
class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls  = ['https://www.qiushibaike.com/8hr/page/1/']
    base_domain ='https://www.qiushibaike.com'    #底层url

    def parse(self, response):
        t = response.xpath("//div[@class='recmd-right']/a[@class='recmd-content']//text()").getall()
        print(t)
        for biaoti in t:
            # item = {"shuju":x}     #利用字典方式传递到pipelines
            item = QsbkItem(biaoti = biaoti)     #创建对象    利用items传递
            yield item     #传递
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()    #提取页数url
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)   #将底层url与页数url拼接


