import scrapy
import json
from ..items import tenDaysItem
import datetime
import time


class tendaysSpider(scrapy.Spider):
    name = 'tenDays'
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.tenDaysPipeline': 3,
        },
        'FILES_STORE': '/opt/input'
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
        # start = response.css('table input[type="radio"]::attr(value)').extract_first()
        # end = '20220412'
        end = getEnd()
        start = getStart(end)
        url = f'http://quotes.money.163.com/service/chddata.html?code={code2}&start={start}&end={end}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        item = tenDaysItem()
        item['file_urls'] = url
        item['name'] = f'{code}_historyTradingData'
        yield item


# 计算end
def getEnd():
    endTime = time.strftime('%Y%m%d',time.localtime(time.time()))
    while 1:
        endTime = datetime.datetime.strptime(endTime, "%Y%m%d")
        p = endTime.isoweekday()
        if p >= 1 and p <= 5:
            break
        endTime = (endTime + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    return endTime.strftime("%Y%m%d")


# 计算10(更正为30)天前start
def getStart(end):
    startTime = datetime.datetime.strptime(end, "%Y%m%d")
    # count = 10 # 倒推count天
    count = 30
    while count:
        startTime = (startTime + datetime.timedelta(days=-1)).strftime("%Y%m%d")
        startTime = datetime.datetime.strptime(startTime, "%Y%m%d")
        p = startTime.isoweekday()
        if p >= 1 and p <= 5 :
            count -= 1
    return startTime.strftime("%Y%m%d")

