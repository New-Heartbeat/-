from selenium import webdriver
import time
from selenium.webdriver.common.by import By

drive = webdriver.Edge()
drive.get(r'https://www.taobao.com/')

# 标签定位
search_input = drive.find_element(By.ID, 'q')
# 标签交互
search_input.send_keys('iPad')

# 点击搜索按钮
btn = drive.find_element(By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')
btn.click()

time.sleep(2)
drive.get(r'https://www.baidu.com')
time.sleep(2)
# 后退
drive.back()

time.sleep(2)

# 前进
drive.forward()

time.sleep(6)
drive.quit()
