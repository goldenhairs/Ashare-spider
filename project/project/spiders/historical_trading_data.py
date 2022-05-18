import scrapy
import json
from ..items import historicalTradingDataItem


class HistoricalTradingDataSpider(scrapy.Spider):
    name = 'historical_trading_data'
    allowed_domains = ['quotes.money.163.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.historicalTradingDataPipeline': 3,
        }
    }

    def start_requests(self):
        with open('stock.json', 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            stock_list = data_dict['stockList']
            for stock in stock_list:
                code = stock['code']
                url = f'http://quotes.money.163.com/trade/lsjysj_{code}.html#01b07'
                yield scrapy.Request(url=url, callback=self.parse, meta={'code': code})

    def parse(self, response):
        code = response.meta.get('code')
        code2 = response.css('script[type="text/javascript"]').re_first("var STOCKCODE = '(.*?)';")
        start = response.css('table input[type="radio"]::attr(value)').extract_first()
        end = '20220412'
        url = f'http://quotes.money.163.com/service/chddata.html?code={code2}&start={start}&end={end}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        item = historicalTradingDataItem()
        item['file_urls'] = url
        item['name'] = f'{code}_historyTradingData'
        yield item

