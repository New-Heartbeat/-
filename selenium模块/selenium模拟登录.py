from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get(r'https://www.qzone.com')
driver.switch_to.frame('login_frame')
pw_login = driver.find_element(By.ID, 'switcher_plogin')
pw_login.click()

username = driver.find_element(By.ID, 'u')
password = driver.find_element(By.ID, 'p')

time.sleep(1)
username.send_keys('525933188')
time.sleep(1)
password.send_keys('123456')
time.sleep(1)

btn = driver.find_element(By.ID, 'login_button')
btn.click()
