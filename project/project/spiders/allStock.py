import scrapy
import time
from ..items import allStockItem
import json


class AllstockSpider(scrapy.Spider):
    # 爬取沪、深、京A股所有股票最基本数据 -- 给其他爬虫提供遍历所有股票服务
    # --all_Stock.json
    name = 'allStock'
    custom_settings = {
        'ITEM_PIPELINES': {
            
        }
    }
    jq_version = '1124'
    sh_max_page = 109
    sz_max_page = 136
    bj_max_page = 5


    def start_requests(self):
        time13 = int(round(time.time()*1000))
        # 沪
        for page in range(1, self.sh_max_page+1):
            # url中“27”好像是随机数都可以
            url = f'http://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery{self.jq_version}026947754317499206_{time13}&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_={time13}'      
            yield scrapy.Request(url=url, callback=self.parse, meta={'category': '上证A股', 'category_index': 'sh'})
        # 深
        for page in range(1, self.sz_max_page+1):
            url = f'http://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery{self.jq_version}026947754317499206_{time13}&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_={time13}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'category': '深证A股', 'category_index': 'sz'})
        # 京
        for page in range(1, self.bj_max_page+1):
            url = f'http://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery{self.jq_version}026947754317499206_{time13}&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_={time13}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'category': '北证A股', 'category_index': 'bj'})
        
    def parse(self, response):
        text = response.css('*').re_first('({.*}})') 
        data_dict = json.loads(text)
        data_list = data_dict['data']['diff']
        for stock_dict in data_list:
            item = allStockItem()
            item['code'] = stock_dict['f12']
            item['category'] = response.meta.get('category')
            item['cur_name'] = stock_dict['f14']
            item['category_index'] = response.meta.get('category_index')
            yield item
        
        
