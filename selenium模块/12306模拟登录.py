from selenium import webdriver
from selenium.webdriver.edge.webdriver import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

edge_options = Options()
edge_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Edge()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')

username = driver.find_element(By.ID, 'J-userName')
password = driver.find_element(By.ID, 'J-password')

time.sleep(1)
username.send_keys('19972912937')
time.sleep(1)
password.send_keys('xxx')
time.sleep(1)
btn = driver.find_element(By.ID, 'J-login')
btn.click()
time.sleep(1)
span = driver.find_element(By.ID, 'nc_1_n1z')

# 浏览器指定标签处截屏保存
driver.find_element(By.XPATH, '//*[@id="slide"]/div').screenshot('./verify.png')

# 解决特征识别
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
driver.execute_script(script)



action = ActionChains(driver)
action.click_and_hold(span)

for i in range(10):
    action.move_by_offset(36, 0).perform()
    time.sleep(1)

action.release()


