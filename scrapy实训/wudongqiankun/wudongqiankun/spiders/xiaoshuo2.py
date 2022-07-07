import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Xiaoshuo2Spider(CrawlSpider):
    name = 'xiaoshuo2'
    allowed_domains = ['www.xbiquge.la']
    start_urls = ['http://www.xbiquge.la/0/15/12962.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.xbiquge.la/\d*/\d*/\d*.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        a = response.xpath("//h1/text()").get()
        print(a)

