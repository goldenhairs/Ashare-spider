import scrapy
import time
import json
from ..items import newPriceItem
import random


class NewpriceSpider(scrapy.Spider):
    # 爬取最新股价爬虫
    name = 'newPrice'
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.newPricePipeline': 4,
        }
    }

    def start_requests(self):
        page_max = 248
        jq_version = 1124
        time13 = int(round(time.time() * 1000))
        for page in range(1, page_max+1):
            random_num = str(random.random()).replace(".", "")
            # url中“17”好像是随机数都可以
            url = f'http://17.push2.eastmoney.com/api/qt/clist/get?cb=jQuery{jq_version}{random_num}_{time13}&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_={time13}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'time13': time13})

    def parse(self, response):
        text = response.css('*').re_first('({.*}})') 
        data_dict = json.loads(text)
        data_list = data_dict['data']['diff']
        for stock_dict in data_list:
            item = newPriceItem()
            item['code'] = stock_dict['f12']
            time13 = response.meta.get('time13')
            item['time'] = time.strftime('%Y-%m-%d %H:%M',time.localtime(int(time13)/1000))
            item['最新价'] = stock_dict['f2']
            item['涨跌幅'] = str(stock_dict['f3']) + "%"
            item['成交量_手'] = stock_dict['f5']
            item['成交额'] = stock_dict['f6']
            yield item
            
