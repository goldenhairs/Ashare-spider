import requests


# url = 'http://www.cninfo.com.cn/new/data/szse_stock.json' 
# response = requests.get(url=url)
# with open('stock.json', 'w', encoding='utf-8') as f:
#     f.write(response.text)

url = 'http://www.cninfo.com.cn/new/data/list-search.json'
response = requests.get(url=url)
with open('information.json', 'w', encoding='utf-8') as f:
    f.write(response.text)