import scrapy


class CnkiSpider(scrapy.Spider):
    name = 'cnki'
    # allowed_domains = ['www.cnki.com']
    start_urls = ['https://webvpn.tjufe.edu.cn/https/77726476706e69737468656265737421e7e056d2243e635930068cb8/?wrdrecordvisit=1667984283000']

    def parse(self, response):
        page_text = response.text
        with open('cnki.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
        # print(page_text)
