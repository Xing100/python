import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    base_url = "https://search.jd.com/Search?keyword=%E7%94%B7%E8%A3%85&wq=%E7%94%B7%E8%A3%85&page={}"
    urls = []
    for i in range(1,99):
        url = base_url.format(i)
        urls.append(url)

    start_urls = urls


    rules = (
        Rule(LinkExtractor(allow=r'//item.jd.com/\d*.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        name = response.xpath("//div [@class='sku-name']/text()").get()

        print(name)


