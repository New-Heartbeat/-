# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:17:06 2022

@author: 魏俊
爬取veer图片网站中微观世界系列的图片：https://www.veer.com/topic/22202/
1.普通爬虫对url一整张页面进行爬取
2.正则取出图片对应的链接
3.爬取链接中的全部内容（因为图片对应链接的内容包含其他元素）
4.正则取出最后的图片对应的链接并进行爬取和存储

注意！！！：由于请求过多可能会导致爬取的内容不一致，从而不能获取到想要的内容，因此用循环运行爬取时要慎重！
"""
# -*- coding: utf-8 -*-


import requests
import re
import os

if __name__ == '__main__':
    
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./veerLibs'):
        os.mkdir('./veerLibs')

    url = 'https://www.veer.com/topic/22202/'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    
    # 1.普通爬虫对url一整张页面进行爬取
    response = requests.get(url=url, headers=headers)
    page_text =response.text
    
    # 保存爬取出的整张页面的内容，可用于后面正则表达式的构建
    with open('./veer2.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    ex1 = '<a class="asset_link draggable" href="(.*?)" target.*?</a>'
    ex2 = '</span></button></div><img alt=".*?" src="(.*?)"'
    
    # 2.正则取出图片对应的链接
    img_src_list = re.findall(ex1, page_text, re.S)
    for src in img_src_list:
        # 3.爬取链接中的全部内容
        img_page_text = requests.get(url = src, headers=headers).text
        img_src = re.findall(ex2, img_page_text, re.S)[0]
        # 4.正则取出最后的图片对应的链接并进行爬取和存储
        img_data = requests.get(url='https:'+img_src, headers=headers).content
        img_name = img_src.split('/')[-1].split('?')[0]
        img_path = './veerLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！')







