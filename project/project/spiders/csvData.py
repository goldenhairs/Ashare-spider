import scrapy
import json
from ..items import csvDataItem


class CsvdataSpider(scrapy.Spider):
    name = 'csvData'
    allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.csvDataPipeline': 1,
        }
    }

    def parse(self, response):
        with open('stock.json', 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            stock_list = data_dict['stockList']
            for stock in stock_list:
                item = csvDataItem()
                code = stock['code']
                item['name'] = f'{code}'
                url = f'http://quotes.money.163.com/service/cwbbzy_{code}.html'
                item['file_urls'] = url
                yield item



