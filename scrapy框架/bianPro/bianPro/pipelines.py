# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class BianproPipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./彼岸动漫.txt', 'w', encoding='gbk')

    def process_item(self, item, spider):
        src = item['src']
        alt = item['alt']
        self.fp.write(alt + ',' + src + '\n')
        return item

    def close_spider(self, spider):
        print('爬虫结束!')
        self.fp.close()


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name = item['alt'] + '.jpg'
        return img_name

    def item_completed(self, results, item, info):
        return item
