import scrapy
import json
from ..items import stockPrice5Item
from time import sleep


class Stockpriceper5Spider(scrapy.Spider):
    # 弃用 --5.json 每5分钟股票数据
    name = '5'
    custom_settings = {
        'ITEM_PIPELINES': {
            
        }
    }
    

    def start_requests(self):
        num = 50 # 爬取最近50个数据
        count = 0 # 已爬取股票个数
        with open('all_stock.json', 'r', encoding='UTF-8') as f:
            data_list = json.load(f)
            for data in data_list:
                count += 1
                code = data['code']
                new_code = str(data['category_index']) + str(code)
                url = f'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={new_code}&scale=5&ma=no&datalen={num}' # num:最大1023
                yield scrapy.Request(url=url, callback=self.parse, meta={"code": code, 'count': count}, dont_filter=True)
                
                    
    def parse(self, response):
        # response返回形式: json列表
        count = response.meta.get('count')
        print(f'正在爬取第{count}支股票!!!')
        data_list = json.loads(response.text)
        item = stockPrice5Item()
        res_list = []
        for data in data_list:
            res_dict = {}
            res_dict['day'] = data['day']
            res_dict['open'] = data['open']
            res_dict['high'] = data['high']
            res_dict['low'] = data['low']
            res_dict['close'] = data['close']
            res_dict['volume'] = data['volume']
            res_list.append(res_dict)
        item['code'] = response.meta.get('code')
        item['information'] = res_list
        yield item
        
        
