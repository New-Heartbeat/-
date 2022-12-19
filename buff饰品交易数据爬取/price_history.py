import requests
import json


url = r'https://buff.163.com/api/market/goods/price_history/buff?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
}
cookie = 'nts_mail_user=xindexintiao_wj@163.com:-1:1; _ntes_nuid=b4592cd6615606bd3cd307a6e458008a; _ntes_nnid=b4592cd6615606bd3cd307a6e458008a,1650463645277; NTES_P_UTID=10CgZclX8FwTRaa8TGxMyktheBIIrqE3|1663313383; Device-Id=jU1QZmoYnmbMstTruuZC; P_INFO=19972912937|1665815198|1|netease_buff|00&99|null&null&null#tij&null#10#0|&0|null|19972912937; remember_me=U1091418331|wPgjEmVxlIs3H1gBKtsU6kJ4unMkrhDa; NTES_PASSPORT=qAZamSW2BA4GhHJ8brXPgHyEMxX7uB0EMiNSJPq0sbavEox_E6mDytUJP2di0TTL.jAWjZHWnFDQf0d2Ns9wcd.8D58xFjJSsrf0swkyfSgwq.gw4TnYlataN667qQKU3dBtI4OcGOrGFt8LQfJcH4OeapbC33P15N3uZWuS8.2_rzG3PshnA6tJnT5jxKa2d; session=1-EnXcsYzCLMOBg4WLHowckYxaEGhdmArQTgBCQHWhWn-62042832771; Locale-Supported=zh-Hans; game=csgo; csrf_token=IjI5YTBiNjhhYzFlMTI1MDUzOGU5NGE0ZmIwMTVhZmJmNTkwZjIxYWMi.FjP2mg.TWYaUD984X5UlWPSnXz10jGfWCw'
goods_id = '42673'
params = {
    'game': 'csgo',
    'goods_id': '763332',
    'currency': 'CNY',
    '_': '1666345211428'
}

response = requests.get(url=url, headers=headers, params=params)
page_text = response.json()


with open('./price_history.json', 'w', encoding='utf-8') as fp:
    json.dump(page_text, fp=fp, ensure_ascii=False)

# tree = etree.HTML(page_text)
# price1 = tree.xpath('//div[@id="relative-goods"]/div/a/span/@data-price')
# title = tree.xpath('//div[@id="relative-goods"]/div/a/text()')
# print(price1)
# print(title)

