import scrapy

class MySpider(scrapy.Spider):
    #用于区别Spider
    name = "MySpider"
    #允许访问的域
    allowed_domains = []
    #爬取的地址
    start_urls = []
    #爬取方法
    def parse(self, response):
        pass