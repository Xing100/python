# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JianshuSpiderPipeline:
    def __init__(self):
        self.fp = open("简书.txt","a",encoding ="utf-8" )


    def process_item(self, item, spider):
        self.fp.write(str(item)+"\n")
        return item
