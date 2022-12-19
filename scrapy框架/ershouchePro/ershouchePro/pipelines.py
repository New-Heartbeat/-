# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ErshoucheproPipeline:
    fp = None

    def open_spider(self, spider):
        print("开始爬虫...")
        self.fp = open('./ershoufang.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        price = item['price']

        self.fp.write(title + ',' + price + '\n')

        return item

    def close_spider(self, spider):
        print('爬虫结束！')
        self.fp.close()


class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='ershoufang',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into ershoufang_temp_1022 values("%s", "%s")' % (item['title'], item['price']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
