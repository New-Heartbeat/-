# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:05:36 2022

@author: 魏俊
"""

import time

# 同步爬虫

# start_time = time.time()

# def get_page(str):
#     print('正在下载：', str)
#     time.sleep(2)
#     print('下载成功：', str)
    
# url_list = ['aa', 'bb', 'cc', 'TaT']

# for url in url_list:
#     get_page(url)

# end_time = time.time()

# print(end_time - start_time)

# 异步爬虫
from multiprocessing.dummy import Pool

start_time = time.time()

def get_page(str):
    # print('正在下载：', str)
    print('正在下载：'+ str)
    time.sleep(2)
    print('下载成功：', str)
    
url_list = ['aa', 'bb', 'cc', 'TaT']

pool = Pool(4)
pool.map(get_page, url_list)

end_time = time.time()

print(end_time - start_time)


