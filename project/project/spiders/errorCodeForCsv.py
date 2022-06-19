import scrapy
import json
import os
from ..items import csvDataItem


class ErrorcodeforcsvSpider(scrapy.Spider):
    name = 'errorCodeForCsv'
    allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.csvDataPipeline': 100,
        }
    }

    def parse(self, response):
        with open('../errorDetection/error_code_list.txt', 'r') as f:
            error_code_list = f.read().split(',')
            for code in error_code_list:
                item = csvDataItem()
                item['name'] = f'{code}'
                url = f'http://quotes.money.163.com/service/cwbbzy_{code}.html'
                item['file_urls'] = url
                yield item