# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:35:48 2022

@author: 魏俊
"""

import requests 
import pytesseract
from PIL import Image

if __name__ == '__main__':

    url = 'https://so.gushiwen.cn/RandCode.ashx'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    
    img_data = requests.get(url=url, headers=headers).content
    with open('验证码.jpg', 'wb') as fp:
        fp.write(img_data)
    
    image = Image.open('验证码.jpg')
    code = pytesseract.image_to_string(image)
    
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    data = {
        '__VIEWSTATE': 'tUBWmbApRRY7kxzKfzVEW+QIkxeh1wpEg1pX1ZaH/B65s/7lAVTxNlPK/hcBw1MoKCceB/XIAJk/z6FH2B5fsg8tetMcKw5LLj/Lex5cVZrvJgnPa4oKKNnXM9pw378xOB97T5UYvLPz4EpGBY4FQPejSWQ=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '525933188@qq.com',
        'pwd': 'a1052614106',
        'code': code,
        'denglu': '登录'
        }
    
    #创建一个session对象
    session = requests.Session()
    
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.status_code)
    page_text = response.text
    
    #爬取当前用户的个人主页对应的页面数据
    detail_url = 'https://so.gushiwen.cn/user/collect.aspx'
    #手动cookie处理
    # headers = {
    #     'Cookie':'xxxx'
    # }
    #使用携带cookie的session进行get请求的发送
    detail_page_text = session.get(url=detail_url,headers=headers).text
    with open('../b站爬取/burningj.html', 'w', encoding='utf-8') as fp:
        fp.write(detail_page_text)



