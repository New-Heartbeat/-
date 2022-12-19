import requests
from lxml import etree
from bs4 import BeautifulSoup
import json


def discount_for_steam_balance(steam_price, buff_price):
    return round(buff_price / (steam_price * 0.85), 3)


def discount_for_buff_balance(steam_price, buff_price):
    return round(buff_price * 0.99 / steam_price, 3)


url = r'https://buff.163.com/api/market/goods/sell_order?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
goods_id = '835470'
params = {
    'game': 'csgo',
    'goods_id': goods_id,
    'page_num': '1',
    'sort_by': 'default',
    'mode': '',
    'allow_tradable_cooldown': 1,
    '_': ''
}

response = requests.get(url=url, headers=headers, params=params)
page_text = response.json()

items = []
name = page_text['data']['goods_infos'][goods_id]['name']
buff_price = float(page_text['data']['items'][0]['price'])
steam_price = float(page_text['data']['goods_infos'][goods_id]['steam_price_cny'])
for_steam_balance = discount_for_steam_balance(steam_price, buff_price)
for_buff_balance = discount_for_buff_balance(steam_price, buff_price)
items.append([name, buff_price, steam_price, for_steam_balance, for_buff_balance])

# with open('./page_json.json', 'w', encoding='utf-8') as fp:
#     json.dump(page_text, fp=fp, ensure_ascii=False)

# tree = etree.HTML(page_text)
# price1 = tree.xpath('//div[@id="relative-goods"]/div/a/span/@data-price')
# title = tree.xpath('//div[@id="relative-goods"]/div/a/text()')
# print(price1)
# print(title)

# soup = BeautifulSoup(page_text, 'lxml')
# price2 = soup.select('#relative-goods > div > a > span')
# print(price2)

# print(name)
# print(buff_price)
# print(steam_price)
print(items)
