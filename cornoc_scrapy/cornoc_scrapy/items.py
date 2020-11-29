# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CornocScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #航空公司图片
    img = scrapy.Field()
    #航空公司地址
    href = scrapy.Field()
    #航班号
    number = scrapy.Field()
    #始发地、目的地
    city = scrapy.Field()
    #停机楼
    terminal = scrapy.Field()
    #预计
    expected = scrapy.Field()
    #实际
    actual = scrapy.Field()
    #状态
    state = scrapy.Field()

    #现在时间(爬取时间)
    nowtime = scrapy.Field()
    
    #pass
