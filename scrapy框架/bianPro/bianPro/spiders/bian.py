import scrapy
from ..items import BianproItem


class BianSpider(scrapy.Spider):
    name = 'bian'
    # allowed_domains = ['www.bian.com']
    start_urls = ['http://pic.netbian.com/4kdongman/']

    def parse(self, response):

        src_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src').extract()
        alt_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@alt').extract()
        for i in range(10):
            item = BianproItem()
            item['src'] = 'http://pic.netbian.com' + src_list[i]
            item['alt'] = alt_list[i]
            # print(item['src'])

            yield item
