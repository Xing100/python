import scrapy



class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['www.x biquge.la']
    start_urls = ['http://www.xbiquge.la/0/15/12961.html']

    def parse(self, response):
        a = response.xpath("//h1/text()").get()
        print(a)
        base_url = "http://www.xbiquge.la/"
        next_url = response.xpath("//div[@class='bottem2']/a[4]//@href").get()
        next_url = base_url + next_url
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
