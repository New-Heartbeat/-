import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BaiduproItem
import re


# class BaiduSpider(CrawlSpider):
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=互联网金融']
    # link = LinkExtractor(allow=r'&rsv_dl=news_b_pn&pn=\d+')
    # rules = (
    #     Rule(link, callback='parse_item', follow=False),
    # )

    # r'https://baijiahao.baidu.com/s?id=1747896103136271278&wfr=spider&for=pc'
    # r'http://www.nbd.com.cn/articles/2022-10-28/2524034.html'

    # def parse_start_url(self, response):
    #     title_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/h3/a/@aria-label').extract()
    #     date_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/div/div/span[1]/text()').extract()
    #     journal_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/div/div/div/a/span/text()').extract()
    #     detail_url_list = response.xpath('//div[@id="content_left"]/div/div/h3/a/@href').extract()
    #     length = len(title_list)
    #     for i in range(length):
    #         item = BaiduproItem()
    #         item['title'] = title_list[i]
    #         item['url'] = response.url
    #         item['date'] = date_list[i]
    #         item['journal'] = journal_list[i]
    #         item['detail_url'] = detail_url_list[i]
    #
    #         yield item

    def parse(self, response):
    # def parse_item(self, response):  # 配合CrawlSpider使用
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        title_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/h3/a/@aria-label').extract()
        date_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/div/div/span[1]/text()').extract()
        journal_list = response.xpath('//div[@class="result-op c-container xpath-log new-pmd"]/div/div/div/div/a/span/text()').extract()
        detail_url_list = response.xpath('//div[@id="content_left"]/div/div/h3/a/@href').extract()
        length = len(title_list)
        for i in range(length):
            item = BaiduproItem()
            item['title'] = title_list[i]
            item['url'] = response.url
            item['date'] = date_list[i]
            item['journal'] = journal_list[i]
            item['detail_url'] = detail_url_list[i]

            # yield item
            yield scrapy.Request(detail_url_list[i], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']

        journal_content = response.text
        result = re.findall(u'[\u4e00-\u9fa5]', journal_content)
        item['content'] = ''.join(result)

        yield item

