import scrapy
import json
from ..items import moneyItem


class MoneySpider(scrapy.Spider):
    name = 'money'
    allowed_domains = ['quotes.money.163.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            
        }
    }
    
    def start_requests(self):
        with open('stock.json', 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            stock_list = data_dict['stockList']
            for stock in stock_list:
                code = stock['code']
                category = stock['category']
                url = f'http://quotes.money.163.com/f10/gszl_{code}.html#01f01'
                yield scrapy.Request(url=url, callback=self.parse, meta={'code': code, 'category': category})

    def parse(self, response):
        item = moneyItem()
        item['code'] = response.meta.get('code')
        item['category'] = response.meta.get('category')
        datas = response.css('.col_l_01 .table_bg001 .td_width160')
        item['组织形式'] = datas.re('>(.*?)</td>')[0]
        item['地域'] = datas.re('>(.*?)</td>')[1]
        item['中文简称'] = datas.re('>(.*?)</td>')[2]
        item['办公地址'] = datas.re('>(.*?)</td>')[3]
        item['公司全称'] = datas.re('>(.*?)</td>')[4]
        item['公司电话'] = datas.re('>(.*?)</td>')[5]
        item['英文名称'] = datas.re('>(.*?)</td>')[6]
        item['公司电子邮箱'] = datas.re('>(.*?)</td>')[7]
        item['注册资本'] = datas.re('>(.*?)</td>')[8]
        item['董事长'] = datas.re('>(.*?)</td>')[9]
        item['员工人数'] = datas.re('>(.*?)</td>')[10]
        item['董事会秘书'] = datas.re('>(.*?)</td>')[11]
        item['法人代表'] = datas.re('>(.*?)</td>')[12]
        item['董秘电话'] = datas.re('>(.*?)</td>')[13]
        item['总经理'] = datas.re('>(.*?)</td>')[14]
        item['董秘传真'] = datas.re('>(.*?)</td>')[15]
        item['信息披露网址'] = datas.re('>(.*?)</td>')[16]
        item['信息披露报纸名称'] = datas.re('>(.*?)</td>')[17]

        item['主营业务'] = response.css('.col_l_01 .table_bg001 td[colspan="3"]::text').extract()[0].strip()
        item['经营范围'] = response.css('.col_l_01 .table_bg001 td[colspan="3"]::text').extract()[1].strip()
        item['公司沿革'] = response.css('.col_l_01 .table_bg001 td[colspan="3"]::text').extract()[2].strip()
        yield item
