import scrapy
from cornoc_scrapy.items import CornocScrapyItem

class MySpider(scrapy.Spider):
    #用于区别Spider
    name = "MySpider"
    #允许访问的域
    allowed_domains = ['data.carnoc.com']
    #爬取的地址
    start_urls = ['http://data.carnoc.com/corp/airport/csx__airportflight.html']
    #爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        arrivaldata = CornocScrapyItem()
        #进港数据
        for li in response.xpath("//div[@id='icefable1']/li"):
            arrivaldata['type'] = "进港"
            arrivaldata['img'] = li.xpath(".//span[1]/a/img/@src").extract()[0]
            arrivaldata['href'] = li.xpath(".//span[1]/a/@href").extract()[0]
            arrivaldata['number'] = li.xpath(".//span[1]/text()").extract()[0]
            arrivaldata['city'] = li.xpath(".//span[2]/text()").extract()[0]
            arrivaldata['terminal'] = li.xpath(".//span[3]/text()").extract()[0]
            arrivaldata['expected'] = li.xpath(".//span[4]/text()").extract()[0]
            arrivaldata['actual'] = li.xpath(".//span[5]/text()").extract()[0]
            arrivaldata['state'] = li.xpath(".//span[6]/text()").extract()[0]
            yield(arrivaldata)

        departuredata = CornocScrapyItem()
        for li in response.xpath("//div[@id='icefable2']/li"):
            departuredata['type'] = "出港"
            departuredata['img'] = li.xpath("./span[1]/a/img/@src").extract()[0]
            departuredata['href'] = li.xpath("./span[1]/a/@href").extract()[0]
            departuredata['number'] = li.xpath("./span[1]/text()").extract()[0]
            departuredata['city'] = li.xpath("./span[2]/text()").extract()[0]
            departuredata['terminal'] = li.xpath("./span[3]/text()").extract()[0]
            departuredata['expected'] = li.xpath("./span[4]/text()").extract()[0]
            departuredata['actual'] = li.xpath("./span[5]/text()").extract()[0]
            departuredata['state'] = li.xpath("./span[6]/text()").extract()[0]
            yield(departuredata)

        pass