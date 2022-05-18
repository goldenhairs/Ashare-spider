import scrapy
import json
import random
import time
from ..items import dailyPriceItem


class DailypriceSpider(scrapy.Spider):
    # 每日每分钟股票接口
    name = 'dailyPrice'
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.dailyPricePipeline': 5,
        }
    }
    

    def start_requests(self):
        jq_version = '1124' # jQuery版本号 
        with open('all_stock.json', 'r', encoding='UTF-8') as f:
            data_list = json.load(f)
            for stock in data_list:
                code = stock['code']
                category_index = stock['category_index']
                if category_index == 'sh':
                    index = 1
                elif category_index == 'sz':
                    index = 0
                elif category_index == 'bj':
                    # 东方财富网暂时没有京A股每分钟K线图,只有每5分钟K线图 
                    continue
                time13 = int(round(time.time()*1000))
                random_num = str(random.random()).replace(".", "")
                url = f'http://push2his.eastmoney.com/api/qt/stock/trends2/get?cb=jQuery{jq_version}{random_num}_{time13}&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6%2Cf7%2Cf8%2Cf9%2Cf10%2Cf11%2Cf12%2Cf13&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&ut=7eea3edcaed734bea9cbfc24409ed989&ndays=1&iscr=0&secid={index}.{code}&_={time13}'
                print(url)
                yield scrapy.Request(url=url, callback=self.parse, meta={'code': code, 'category_index': category_index})

    def parse(self, response):
        text = response.css('*').re_first('({.*}})') 
        data_dict = json.loads(text)
        data_list = data_dict['data']['trends']

        item = dailyPriceItem()
        item['code'] = response.meta.get('code')
        item['category_index'] = response.meta.get('category_index')
        item['name'] = data_dict['data']['name']

        trend_list = []
        for data in data_list:
            temp_dict = {}
            d_list = data.split(',')
            temp_dict['时间'] = d_list[0]
            temp_dict['当前价格'] = d_list[2]
            temp_dict['成交量'] = d_list[5]
            trend_list.append(temp_dict)

        item['trends'] = trend_list
        yield item