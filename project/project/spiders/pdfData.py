import scrapy
import json
from ..items import pdfDataItem
import time


class PdfdataSpider(scrapy.Spider):
    name = 'pdfData'
    allowed_domains = ['quotes.money.163.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.pdfDataPipeline': 2,
        }
    }

    def start_requests(self):
        with open('stock.json', 'r', encoding='UTF-8') as f:
            data_dict = json.load(f)
            stock_list = data_dict['stockList']
            for stock in stock_list:
                code = stock['code']
                orgId = stock['orgId']
                url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
                for page in range(2):
                    query = {
                        'stock': f'{code},{orgId}',
                        'tabName': 'fulltext',
                        'pageSize': '30',
                        'pageNum': f'{page}',
                        # 'column': 'sse', # 所以说不需要完整的数据就可以post
                        'category': 'category_ndbg_szsh',
                        # 'plate': 'sh',
                        'seDate': '',
                        'searchkey': '',
                        'secid': '',
                        'sortName': '',
                        'sortType': '',
                        'isHLtitle': 'true'
                    }
                    yield scrapy.FormRequest(url=url, formdata=query, callback=self.parse)

    def parse(self, response):
        dic = response.json()
        for data in dic['announcements']:
            item = pdfDataItem()
            id = data['announcementId']
            code = data['secCode']
            name = data['secName']
            title = data['announcementTitle']
            aTime = data['announcementTime']
            stockTime = time.strftime('%Y-%m-%d', time.localtime(aTime/1000))
            # bulletinId就是announcementId
            # announceTime 13位数字是时间戳 可以转换为日期数据
            url = f'http://www.cninfo.com.cn/new/announcement/download?bulletinId={id}&announceTime={stockTime}'
            item['name'] = f'{code}_{name}_{title}'
            item['file_urls'] = url
            yield item
