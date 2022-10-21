import time
from selenium.webdriver.edge.webdriver import Options
from selenium import webdriver

# 无可视化界面
edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument('headless')  # 实现无头
edge_options.add_argument('--disable-blink-features=AutomationControlled')  # 规避检测，即在浏览器控制台输入alert(window.navigator.webdriver)结果为false

driver = webdriver.Edge(options=edge_options)
driver.get('https://www.baidu.com')
time.sleep(5)

print(driver.page_source)
driver.quit()

