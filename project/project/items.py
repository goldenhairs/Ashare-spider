# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from fileinput import close
from scrapy import Item, Field


class allStockItem(Item):
    cur_name = Field()
    category = Field() 
    code = Field()
    category_index = Field()


class dailyPriceItem(Item):
    code = Field()
    category_index = Field()
    name = Field()
    trends = Field()


class moneyItem(Item):
    code = Field()
    category = Field()
    中文简称 = Field()
    组织形式 = Field()
    地域 = Field()
    办公地址 = Field()
    公司全称 = Field()
    公司电话 = Field()
    英文名称 = Field()
    公司电子邮箱 = Field()
    注册资本 = Field()
    董事长 = Field()
    员工人数 = Field()
    董事会秘书 = Field()
    法人代表 = Field()
    董秘电话 = Field()
    总经理 = Field()
    董秘传真 = Field()
    信息披露网址 = Field()
    信息披露报纸名称 = Field()
    主营业务 = Field()
    经营范围 = Field()
    公司沿革 = Field()


class csvDataItem(Item):
    name = Field()
    file_urls = Field()
    files = Field()


class pdfDataItem(Item):
    name = Field()
    file_urls = Field()
    files = Field()


class historicalTradingDataItem(Item):
    name = Field()
    file_urls = Field()
    files = Field()


class newCodeItem(Item):
    code = Field()
    new_code = Field()


class stockPrice5Item(Item):
    code = Field()
    information = Field()


class newPriceItem(Item):
    code = Field()
    time = Field()
    最新价 = Field()
    涨跌幅 = Field()
    成交量_手 = Field()
    成交额 = Field()


class testItem(Item):
    text = Field()