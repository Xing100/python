# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WxappPipeline:
    def __init__(self):
        self.fp = open("title.txt","a",encoding="utf-8")     #打开文件

    def open_spider(self,spider):
        print("爬虫开始了")

    def process_item(self, item, spider):
        self.fp.write(str(item)+"\n")
        return item

    def open_spider(self,spider):
        print("爬虫结束了")
