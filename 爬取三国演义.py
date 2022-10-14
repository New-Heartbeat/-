# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:52:12 2022

@author: 魏俊
需求：爬取《三国演义》小说所有的章节标题和章节内容https://www.shicimingju.com/book/sanguoyanyi.html
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    page_text_res = requests.get(url=url, headers=headers)
    page_text_res.encoding = 'utf-8'
    page_text = page_text_res.text
    soup = BeautifulSoup(page_text, 'lxml')
    select_list = soup.select('.book-mulu > ul > li > a')
    url_assist = 'https://www.shicimingju.com'
    
    fp = open('./sanguoyanyi.txt', 'w', encoding='utf-8')
    for select in select_list:
        title = select.string
        chapter_url = url_assist + select['href']
        res = requests.get(url=chapter_url, headers=headers)
        res.encoding = 'utf-8'
        text = res.text
        chapter_soup = BeautifulSoup(text, 'lxml')
        chapter_content = chapter_soup.find('div', class_='chapter_content').text
        fp.write(title+':'+chapter_content+'\n')
        print(title, "爬取成功")
        # print(select.string, '链接：', url_assist + select['href'], '爬取成功')
    
    
    
    print('over')



