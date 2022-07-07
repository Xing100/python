import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[a-z0-9]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title =response.xpath("//h1[@class='_1RuRku']/text()").get()
        zuozhe = response.xpath("//span[@class='_22gUMi']/text()").get()
        neirong = response.xpath("//article[@class='_2rhmJa']").get()
        item = JianshuSpiderItem(title = title,zuozhe = zuozhe,neirong = neirong)
        yield item