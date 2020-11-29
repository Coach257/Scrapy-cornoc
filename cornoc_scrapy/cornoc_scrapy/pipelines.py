# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class CornocScrapyPipeline:
    def __init__(self):
        #打开文件
        self.file = open('../data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        #数据清洗：过滤无效数据
        if len(item)!=9:
            return "invalid data!!!\n"
        #输出对象转json
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        #写入json文件
        self.file.write(line)
        return item



     #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass
