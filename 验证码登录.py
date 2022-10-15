# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:06:52 2022

@author: 魏俊
"""

import requests

if __name__ == '__main__':
    
    url = 'https://so.gushiwen.cn/RandCode.ashx'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    
    img_data = requests.get(url=url, headers=headers).content
    with open('./验证码.jpg', 'wb') as fp:
        fp.write(img_data)
    
    print('over')






