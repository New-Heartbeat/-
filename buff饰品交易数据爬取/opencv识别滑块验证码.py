from io import BytesIO
from PIL import Image
import cv2
import numpy as np

# 读取背景图片和缺口图片
bg_img = cv2.imread('bg_code.jpg')  # 背景图片
tp_img = cv2.imread('lost_code.jpg')  # 缺口图片

# 识别图片边缘
bg_edge = cv2.Canny(bg_img, 100, 200)
tp_edge = cv2.Canny(tp_img, 100, 200)

# 转换图片格式
bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

# 缺口匹配
res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

# 绘制方框
th, tw = tp_pic.shape[:2]
tl = max_loc  # 左上角点的坐标
br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
cv2.imwrite('out.jpg', bg_img)  # 保存在本地

x = tl[0]
print(x)
