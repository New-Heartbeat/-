# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:20:34 2022

@author: 魏俊
"""

import requests
from lxml import etree

if __name__ == '__main__':
    
    url = 'https://tj.58.com/ershouche/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    
    page_text = requests.get(url=url, headers=headers).text
    # with open('./ershouche.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    tree = etree.HTML(page_text)
    r = tree.xpath('//div[@class="info--desc"]/h2//text()')
    
    

    
    print(r)



