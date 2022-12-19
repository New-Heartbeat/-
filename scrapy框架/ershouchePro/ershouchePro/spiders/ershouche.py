import scrapy
from ..items import ErshoucheproItem

class ErshoucheSpider(scrapy.Spider):
    name = 'ershouche'
    # allowed_domains = ['tj.58.com']
    start_urls = ['https://tj.58.com/ershoufang/']

    # 终端指令存储
    # def parse(self, response):
    #     dic = []
    #     title = response.xpath('//section[@class="list"][1]/div/a/div[2]/div/div/h3/@title').extract()
    #     price = response.xpath('//section[@class="list"][1]/div/a/div[2]/div[2]/p[1]/span[1]/text()').extract()
    #     length = len(title)
    #     for i in range(30):
    #         data = {
    #             'title': title[i],
    #             'price': price[i]
    #         }
    #         dic.append(data)
    #
    #     # print(dic)
    #     return dic

    # 管道化存储
    def parse(self, response):
        title = response.xpath('//section[@class="list"][1]/div/a/div[2]/div/div/h3/@title').extract()
        price = response.xpath('//section[@class="list"][1]/div/a/div[2]/div[2]/p[1]/span[1]/text()').extract()
        item = ErshoucheproItem()
        for i in range(20):
            item['title'] = title[i]
            item['price'] = price[i]

            yield item
