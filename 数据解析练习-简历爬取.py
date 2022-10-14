# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:37:38 2022

@author: 魏俊
"""

import requests 
from lxml import etree
import os

if __name__ == '__main__':
    
    # 创建文件夹存储批量爬取的简历模板
    dir_name = './jianliLib'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }   
    # 分页下载20页
    for i in range(2,22):
        url = 'https://sc.chinaz.com/jianli/free_%d.html'%i
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        src_list = tree.xpath('//div[@id="main"]/div/div/a/@href')
        for src in src_list:
            if src.startswith('http') == 0:
                src = 'https:' + src # 第二页的page_text中用xpath解析的链接少'https:'
            detail_page_text = requests.get(url=src, headers=headers).text
            detail_tree = etree.HTML(detail_page_text)
            jianli_name = detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')
            jianli_name = jianli_name[0].encode('iso-8859-1').decode('utf-8')
            download_url = detail_tree.xpath('//ul[@class="clearfix"]/li[1]/a/@href')
            jianli_data = requests.get(url=url, headers=headers).content
            with open(dir_name+'/'+jianli_name+'.rar', 'wb') as fp:
                fp.write(jianli_data)
            print(jianli_name, '下载成功')
        print('第%d页下载成功'%i)
    
    # 测试爬取下载链接获取的内容
    # 压缩包为二进制文件，像图片一样用content接收即可
    # url = 'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli564.rar'
    # jianli_data = requests.get(url=url, headers=headers).content
    # with open('./jianli_test.rar', 'wb') as fp:
    #     fp.write(jianli_data)
    
    
    
    print('over')














