# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:54:38 2022

@author: 魏俊
"""

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from requests import get
from PIL import Image
# import pytesser3  # 注意，要安装tesseract
import pytesseract
from io import BytesIO  # 内存IO，将数据写入到内存中去，不会产生文件

img_url = "https://so.gushiwen.cn/RandCode.ashx"  # 生成验证码的网址
# img_data = BytesIO(get(img_url).content)  # 里面传入二进制数据
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
img_data = get(img_url, headers=headers).content
with open('验证码.jpg', 'wb') as fp:
    fp.write(img_data)
img = Image.open('验证码.jpg')  # 打开验证码图片
img = img.convert("L")  # 将图片转换为灰度图
# 获取阈值阈值可以通过数组来获取，这里默认方便，默认阈值为175
avg = 175

# threshold = 180
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# photo = img.point(table, '1')  #图片二值化
#保存处理好的图片
# photo.save('./验证码new.jpg')
# image = Image.open('./验证码new.jpg')

# 二值化处理
w, h = img.size  # 获取图片的大小
pixes = img.load()  # 获取照片的像素
for x in range(w):
    for y in range(h):
        if pixes[x, y] < avg:
            pixes[x, y] = 0
        else:
            pixes[x, y] = 255
# 去除噪点
for x in range(1, w - 1):
    for y in range(1, h - 1):
        count = 0  # 统计周边摆设像素的个数
        if pixes[x, y - 1] > 245:  # 如果上面的像素的颜色为白色
            count += 1
        if pixes[x, y + 1] > 245:  # 如果下面的像素的颜色白色
            count += 1
        if pixes[x - 1, y] > 245:  # 如果左边的像素的颜色为白色
            count += 1
        if pixes[x + 1, y] > 245:  # 如果右边的像素的颜色为白色
            count += 1
        if pixes[x - 1, y - 1] > 245:  # 如果左上面的像素的颜色为白色
            count += 1
        if pixes[x - 1, y + 1] > 245:  # 如果左下面的像素的颜色为白色
            count += 1
        if pixes[x - 1, y + 1] > 245:  # 如果右下边的像素的颜色为白色
            count += 1
        if pixes[x + 1, y - 1] > 245:  # 如果右上边的像素的颜色为白色
            count += 1
        if count > 5:
            pixes[x, y] = 255  # 如果有超过5个像素点的颜色为白色，说明很可能是一个噪点

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\tesseract-ocr\tesseract.exe"
result = pytesseract.image_to_string(img) # 使用该方法，将图片内容转换为文字
print(result)  
# img.show()

