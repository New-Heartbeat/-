# -*- coding: utf-8 -*-
"""
Created on 2022.10.16 18:34

@author: 魏俊
"""
import requests
import json
from lxml import etree

if __name__ == '__main__':
    
    url = 'https://www.bilibili.com/video/BV1e14y177q2/?vd_source=135905d3089450e512648e8393b17cef'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
        }
    # data = {
    #     '__refresh__': 'true',
    #     '_extra': '',
    #     'context': '',
    #     'page': 1,
    #     'page_size': 42,
    #     'order': '',
    #     'duration': '',
    #     'from_source': '',
    #     'from_spmid': 333.337,
    #     'platform': 'pc',
    #     'highlight': 1,
    #     'single_column': 0,
    #     'keyword': 'apex',
    #     'qv_id': 'w9uSTtKvAuYUr8LxHjGK4TXHSVhuNv5G',
    #     'preload': 'true',
    #     'com2co': 'true',
    #     'cookie':"buvid3=932F61FE-0CC6-0D11-7D08-E0916E46FB9300676infoc; i-wanna-go-back=-1; _uuid=C162EA1D-8DAB-1164-B3D10-10B644EBBBFB600947infoc; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; rpdid=|(k)~YR|)||u0J'uYR~)Yl|ll; nostalgia_conf=-1; LIVE_BUVID=AUTO6416480029391118; hit-dyn-v2=1; fingerprint3=bb26445d6d696272a50488cda06bfe8a; CURRENT_QUALITY=80; buvid4=5E52087F-A85D-622E-37C7-A2A527AB371701527-022032119-qWxGLI%2FYLlU62tKPbzxjTw%3D%3D; b_nut=100; fingerprint=73aa02a9c6f685f3362e972d04f9621f; SESSDATA=10944f4c%2C1681403458%2C480a3%2Aa1; bili_jct=b1b65564ee1eb6db7f7fca05caab0118; DedeUserID=47378096; DedeUserID__ckMd5=949c1a3254486d65; sid=64u45sbo; buvid_fp=73aa02a9c6f685f3362e972d04f9621f; PVID=2; b_ut=5; bp_video_offset_47378096=717555053828767900; innersign=1; CURRENT_FNVAL=16; b_lsid=5D3ADBF7_183E066ACB0"
    #     }
    
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    
    #持久化存储
    # fileName = './bilibilivideo.json'
    # fp = open(fileName,'w',encoding='utf-8')
    # json.dump(page_text,fp=fp,ensure_ascii=False)
    
    
    with open('./bilibilivideo.html', 'w') as fp:
        fp.write(page_text)
    
    print('over')




















