# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:13:06 2022

@author: 魏俊

直接爬取b站空间

"""

# import requests
# import pytesseract
# from PIL import Image
# import pymysql


# url = 'https://space.bilibili.com/35359510/dynamic'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
# }
#
# response = requests.get(url=url, headers=headers)
# page_text = response.text
# with open('./bilibilispace.html', 'w') as fp:
#     fp.write(page_text)
#
# print(response.status_code)

# from sklearn.feature_extraction.text import TfidfVectorizer
#
# import pandas as pd
#
#
# corpus = ["纺织 非遗 刺绣 非物质文化遗产",
#           "织染 文化 技艺 传承人 色彩",
#           "织染 文化 技艺 传承人 色彩"]
#
# df1 = pd.DataFrame(corpus, columns=['Text'])
#
# vectorize = TfidfVectorizer()
# dtm = vectorize.fit_transform(corpus)
# df2 = pd.DataFrame(dtm.toarray(),
#              columns=vectorize.get_feature_names())
# print(df2)

# import sys
# print(sys.path)

# from scipy._lib._util import _rename_parameter
#
# from sklearn.feature_extraction.text import TfidfVectorizer


import requests
import re

# 1、对单个页面进行请求，并返回数据信息——通过data自定义特定企业
def get_and_download_pdf_flie(pageNum, stock, searchkey='', category='', seDate=''):
    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    pageNum = int(pageNum)
    #   定义表单数据
    data = {'pageNum': pageNum,
            'pageSize': 30,
            'column': 'szse',
            'tabName': 'fulltext',
            'plate': '',
            'stock': stock,
            'searchkey': searchkey,
            'secid': '',
            'category': category,
            'trade': '',
            'seDate': seDate,
            'sortName': '',
            'sortType': '',
            'isHLtitle': 'true'}

    #   定义请求头
    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content-Length': '181',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Host': 'www.cninfo.com.cn',
               'Origin': 'http://www.cninfo.com.cn',
               'Referer': 'http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}

    #   提交请求
    r = requests.post(url, data=data, headers=headers)

    #   获取单页年报的数据，数据格式为json，解析并获取json中的年报信息
    result = r.json()['announcements']

    # 2.对数据信息进行提取
    for i in result:
        #         避免下载一些年报摘要等不需要的文件
        if re.search('摘要', i['announcementTitle']):
            pass
        else:
            title = i['announcementTitle']

            #             获取公告文件名，并在下载前将公告文件名中带*号的去掉，因为文件命名规则不能带*号，否则程序会中断
            secName = i['secName']
            secName = secName.replace('*', '')

            #             获取公司股票代码
            secCode = i['secCode']

            #             获取adjunctUrl，并组合生成pdf文件下载地址（分析得知巨潮资讯数据库pdf下载地址格式：http://static.cninfo.com.cn/+adjunctUrl）
            adjunctUrl = i['adjunctUrl']
            down_url = 'http://static.cninfo.com.cn/' + adjunctUrl

            #            定义下载之后需要保存到本地的文件名
            filename = f'{secCode}{secName}{title}.pdf'

            #             定义文件存放地址
            filepath = saving_path + '\\' + filename

            #             提交下载请求
            r = requests.get(down_url)

            #             用response.content来写入文件信息
            with open(filepath, 'wb') as f:
                f.write(r.content)

            #             设置进度条
            print(f'{secCode}{secName}{title}下载完毕')



url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
#   定义表单数据
data = {'pageNum': 1,
        'pageSize': 30,
        'column': 'szse',
        'tabName': 'fulltext',
        'plate': '',
        'stock': '',
        'searchkey': '',
        'secid': '',
        'category': '',
        'trade': '',
        'seDate': '',
        'sortName': '',
        'sortType': '',
        'isHLtitle': 'true'}

#   定义请求头
headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Content-Length': '181',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Host': 'www.cninfo.com.cn',
           'Origin': 'http://www.cninfo.com.cn',
           'Referer': 'http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

#   提交请求
r = requests.post(url, data=data, headers=headers)

#   获取单页年报的数据，数据格式为json，解析并获取json中的年报信息
result = r.json()['announcements']
print(result)
















