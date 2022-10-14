# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:24:18 2022

@author: 魏俊
"""

import requests
from lxml import etree
import os

if __name__ == '__main__':
    
    if not os.path.exists('./bianLibs'):
        os.mkdir('./bianLibs')
    
    url = 'http://pic.netbian.com/4kdongman/'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    
    res = requests.get(url=url, headers=headers)
    res.encoding='gbk'
    page_text = res.text
    tree = etree.HTML(page_text)
    src_list = tree.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    alt_list = tree.xpath('//ul[@class="clearfix"]/li/a/img/@alt')
    img_num = len(src_list)
    src_assist = 'http://pic.netbian.com'
    for i in range(img_num):
        img_url = src_assist + src_list[i]
        img_name = alt_list[i]
        img_data = requests.get(url=img_url, headers=headers).content
        with open('./bianLibs/'+img_name+'.jpg', 'wb') as fp:
            fp.write(img_data)
        print(img_name, "爬取成功")
    
    print('over')







