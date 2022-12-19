import scrapy
from ..items import QidianproItem


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    # allowed_domains = ['www.diqian.com']
    start_urls = ['https://www.qidian.com/rank/collect/page1/']

    # 生成一个通用的url模板
    url = 'https://www.qidian.com/rank/collect/page%d/'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[6]/div[2]/div[2]/div/div/ul/li')
        for li in li_list:
            item = QidianproItem()  # 注意：item对象要在循环里面定义
            title = li.xpath('./div[2]/h2/a/text()').extract()[0]
            author = li.xpath('./div[2]/p[1]/a[1]/text()').extract()[0]
            img_src = li.xpath('./div[1]/a/img/@src').extract()[0]
            item['title'] = title
            item['author'] = author
            item['src'] = 'https:' + img_src
            # print(item['src'])
            yield item

        if self.page_num <= 2:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送：callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
