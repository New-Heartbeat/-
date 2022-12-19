# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import itertools
import xlwt
import json


class BaiduproPipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./百度新闻.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        date = item['date']
        journal = item['journal']
        content = item['content']
        detail_url = item['detail_url']
        # self.fp.write(title + ' ' + detail_url + ' ' + date + ' ' + journal + '\n' + content + '\n')
        json.dump(content, self.fp, ensure_ascii=False)
        self.fp.write("\n")
        return item

    def close_spider(self, spider):
        print('爬虫结束！')
        self.fp.close()


# class CsvPipeline(object):
#     def __init__(self):
#         self.writer = csv.writer(open('百度新闻-金融科技.csv', 'w+', newline=''))
#         # 设置标题
#         self.writer.writerow(['title', 'url', 'date', 'journal'])
#
#     def process_item(self, item, spider):
#         rows = zip(item['title'], item['url'], item['date'], item['journal'])
#         for row in rows:
#             self.writer.writerow(row)
#
#         return item


class ExcelPipeline(object):
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet('互联网金融')
        self.info_list = ['title', 'url', 'date', 'journal']
        self.row = 1

    def open_spider(self, spider):
        print('开始爬虫...')
        for index, info in enumerate(self.info_list):
            self.sheet.write(0, index, info)

    def process_item(self, item, spider):

        data_list = [item["title"], item["url"], item["date"], item["journal"]]

        for index, data in enumerate(data_list):
            self.sheet.write(self.row, index, data)
        self.row += 1
        return item

    def close_spider(self, spider):
        print('爬虫结束！')
        self.workbook.save("百度新闻文本挖掘.xlsx")
