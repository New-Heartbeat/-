from selenium import webdriver
import time
from lxml import etree


driver = webdriver.Edge()
driver.get(r'https://pic.netbian.com/4kdongman/')
page_text = driver.page_source

tree = etree.HTML(page_text)
title_list = tree.xpath('//div[@class="slist"]/ul[1]/li/a/img/@alt')
for title in title_list:
    print(title)

time.sleep(5)

driver.close()






