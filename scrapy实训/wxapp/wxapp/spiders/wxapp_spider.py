import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp.dreawer.com']
    start_urls = ['http://wxapp.dreawer.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'http://wxapp.dreawer.com/portal.php?mod=list&catid=2&page=\d'), follow=True),
          #获取页数url

        Rule(LinkExtractor(allow=r'http://wxapp.dreawer.com/article-\d+-\d.html'),callback="parse_item", follow=False),
    )      #获取页数url      callback将内容返回给parse_item函数处理     follow判断是否跟进

    def parse_item(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()   #解析
        item = WxappItem(title = title)     #创建对象
        yield item   #将item传递给  items.py
