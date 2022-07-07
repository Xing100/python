# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from urllib import request
class BmtpPipeline:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"images")  #将bmtp目录与images拼接
        if not os.path.exists(self.path):    #判断是否有该目录
            os.makedirs(self.path)
    def process_item(self, item, spider):
        title = item["title"]    #将item传入pipelines通道
        urls = item["urls"]

        title_path = os.path.join(self.path,title)    #将images目录与title_path拼接
        if not os.path.exists(title_path):    #判断是否有该目录
            os.makedirs(title_path)
        for url in urls:
            img_name = url.split("__")[-1]
            request.urlretrieve(url,os.path.join(title_path,img_name))    #url   链接地址    os.path.join(title_path,img_name)下载的目录
        return item







