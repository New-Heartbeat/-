# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:13:06 2022

@author: 魏俊

直接爬取b站空间

"""

import requests 
# import pytesseract
# from PIL import Image


url = 'https://space.bilibili.com/35359510/dynamic'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}

response = requests.get(url=url, headers=headers)
page_text = response.text
with open('./bilibilispace.html', 'w') as fp:
    fp.write(page_text)
    
print(response.status_code)




