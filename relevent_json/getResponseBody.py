from telnetlib import SE
import requests
import json
from scrapy import Selector


url = 'http://push2.eastmoney.com/api/qt/stock/trends2/get?cb=jQuery11240473841918081636_1651073065071&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6%2Cf7%2Cf8%2Cf9%2Cf10%2Cf11%2Cf12%2Cf13&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&ut=fa5fd1943c7b386f172d6893dbfba10b&ndays=1&iscr=0&iscca=0&secid=1.600519&_=1651073065096'
response = requests.get(url=url)
# print(type(response.content)) # bytes形式
# print(type(response.text)) # str形式
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(response.text)
selector = Selector(text=response.text)
data = selector.css('*').re_first('({.*}})')
# with open('b.txt', 'w', encoding='utf-8') as fp:
#     fp.write(data)