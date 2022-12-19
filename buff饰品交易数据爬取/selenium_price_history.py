from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import Options
import requests
import time
from selenium.webdriver import ActionChains
import cv2


# 无可视化界面
edge_options = Options()
edge_options.use_chromium = True
# edge_options.add_argument('headless')  # 实现无头
edge_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Edge()
driver.get(r'https://buff.163.com/account/login?back_url=/user-center/asset/recharge/%3F')
time.sleep(1)
driver.find_element(By.XPATH, r'/html/body/div[4]/div[2]/div/div[2]/div[1]/span/i').click()
time.sleep(1)
driver.find_element(By.XPATH, r'/html/body/div[4]/div[2]/div/div[2]/div[2]/span/i').click()
time.sleep(1)

# 坑1：frame的id是可变的，导致解析时不能通过id来定位
frame = driver.find_element(By.XPATH, r'/html/body/div[4]/div[2]/div/div[1]/iframe')
driver.switch_to.frame(frame)
time.sleep(1)

# 坑2：密码登录按钮的id也是可变的
pwd_login = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[1]/a')
pwd_login.click()
time.sleep(1)
driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/input').send_keys('19972912937')
time.sleep(1)
driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[4]/div[2]/input[2]').send_keys('a1052614106')
time.sleep(1)
bg_img_url = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[5]/div/div/div[1]/div/div[1]/img[1]').get_attribute('src')
lost_img_url = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[5]/div/div/div[1]/div/div[1]/img[2]').get_attribute('src')
bg_img_data = requests.get(url=bg_img_url).content
lost_img_data = requests.get(url=lost_img_url).content
with open('./bg_code.jpg', 'wb') as fp:
    fp.write(bg_img_data)
with open('./lost_code.jpg', 'wb') as fp:
    fp.write(lost_img_data)


def identify_gap(bg_img_data, lost_img_data):
    # 读取背景图片和缺口图片
    bg_img = cv2.imread('./bg_code.jpg')  # 背景图片
    tp_img = cv2.imread('./lost_code.jpg')  # 缺口图片

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
    return x


x = identify_gap(bg_img_data, lost_img_data)
span = driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[5]/div/div/div[2]/div[2]')
action = ActionChains(driver)
action.click_and_hold(span)
action.move_by_offset(30, 0).perform()

n = round((x - 30)/10)
for i in range(n):
    action.move_by_offset(10, 0).perform()
    time.sleep(0.2)
residual = x - 30 - n*10
action.move_by_offset(residual, 0)
action.release().perform()
driver.find_element(By.XPATH, r'/html/body/div[2]/div[2]/div[2]/form/div/div[7]/a').click()
time.sleep(1)

driver.get(r'https://buff.163.com/goods/871747#tab=price-chart')



