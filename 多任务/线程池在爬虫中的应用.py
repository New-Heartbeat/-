# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:33:13 2022

@author: 魏俊
"""

import requests
from lxml import etree
import os
import random
import re
from multiprocessing import Pool
import time

start_time = time.time()

# 创建文件夹
dir_name = '../pearvideoLib'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}


def get_page(url):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text


def get_content(video_dict):
    url = video_dict['url']
    title = video_dict['name']
    print(title, '正在爬取')  # get请求是一个耗时的任务，把打印放在前面可以体现多线程的的作用
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        with open(dir_name + '/' + title + '.mp4', 'wb') as fp:
            fp.write(response.content)
        print(title, '爬取成功')
        return response.content


main_url = 'https://www.pearvideo.com/category_1'
main_page_text = get_page(main_url)
main_tree = etree.HTML(main_page_text)
detail_url_list = main_tree.xpath('//div[@class="vervideo-bd"]/a/@href')
detail_title_list = main_tree.xpath('//div[@class="vervideo-bd"]/a/div[2]/text()')
video_cnt = len(detail_url_list)
video_url_list = []
for i in range(2):
    refer_url = 'https://www.pearvideo.com/' + detail_url_list[i]
    url = 'https://www.pearvideo.com/videoStatus.jsp?'
    video_id = re.findall('\d+', detail_url_list[i])[0]
    # detail_page = get_page(url)
    # detait_tree = etree.HTML(detail_page)
    # video_url = detait_tree.xpath('//div[@id="detailsbd"]/div[1]/div[1]/div[1]/div[1]/div[1]/video/@src')
    # 这里网页元素和爬虫爬取到的page_text有差异，因此xpath结果为空
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
        'Referer': refer_url
    }
    params = {
        'contId': video_id,
        'mrd': random.random()
    }
    response = requests.get(url=url, headers=headers, params=params)
    result = response.json()

    fake_link = result['videoInfo']['videos']['srcUrl']
    first_url = os.path.dirname(fake_link)  # https://video.pearvideo.com/mp4/adshort/20201117
    last_url = os.path.basename(fake_link)  # 1665935070145-15487069_adpkg-ad_hd.mp4
    true_part = re.match('^\d+(.*)', last_url).group(1)  # -15299927_adpkg-ad_hd.mp4
    true_url = first_url + '/cont-' + video_id + true_part
    video_dict = {
        'url': true_url,
        'name': detail_title_list[i]
    }
    video_url_list.append(video_dict)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_content, video_url_list)

    end_time = time.time()

    print(end_time - start_time)
# print('over')
