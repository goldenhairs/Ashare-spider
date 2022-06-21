from textwrap import indent
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import CsvItemExporter
import time


class csvDataPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['file_urls'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        name = request.meta['name']
        return f'/财务报表/CSV/{name}.csv'


class pdfDataPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['file_urls'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        name = request.meta['name']
        return f'/财务报表/PDF/{name}.pdf'


class historicalTradingDataPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['file_urls'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        name = request.meta['name']
        return f'/历史交易数据/{name}.csv'


class tenDaysPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['file_urls'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        name = request.meta['name']
        return f'{name}_historyTradingData.csv'


class newPricePipeline:
    def __init__(self):
        pass
    
    def open_spider(self, spider):
        time_tuple = time.localtime(time.time())
        year = time_tuple[0]
        month = time_tuple[1]
        day = time_tuple[2]
        hour = time_tuple[3]
        sec = time_tuple[4]
        self.fp = open(f"实时股价/数据/{year}_{month}_{day}/{year}_{month}_{day}_{hour}_{sec}.json", "wb")
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8', indent=4)
        self.exporter.start_exporting()
    
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()


class dailyPricePipeline:
    def __init__(self):
        pass
    
    def open_spider(self, spider):
        time_tuple = time.localtime(time.time())
        year = time_tuple[0]
        month = time_tuple[1]
        day = time_tuple[2]
        self.fp = open(f"实时股价/每日数据/{year}_{month}_{day}.json", "wb")
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8', indent=4)
        # self.exporter = CsvItemExporter(self.fp)
        self.exporter.start_exporting()
        
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()