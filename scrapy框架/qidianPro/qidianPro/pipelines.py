# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.pipelines.images import ImagesPipeline


class QidianproPipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./起点收藏榜.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        self.fp.write(title + '：' + author + '\n')

        return item

    def close_spider(self, spider):
        print('爬虫结束！')
        self.fp.close()


# class MysqlPipeline:
#     conn = None
#     cursor = None
#
#     def open_spider(self, spider):
#         self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='ershoufang',
#                                     charset='utf8')
#
#     def process_item(self, item, spider):
#         self.cursor = self.conn.cursor()
#         try:
#             self.cursor.execute('insert into ershoufang_temp_1022 values("%s", "%s")' % (item['title'], item['author']))
#             self.conn.commit()
#         except Exception as e:
#             print(e)
#             self.conn.rollback()
#
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()


class ImgPipeline(ImagesPipeline):

    # 可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None, *, item):
        img_name = item['title'] + '.jpg'
        return img_name

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类
