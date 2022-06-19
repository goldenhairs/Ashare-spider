# csv文件下载时出现错误: 财务报表(✔)-网页源代码(×)
# 此脚本用于筛选下载错误的文件至errorCsv.json中
import json
import os

error_code_dict = list()

with open('../spiders/stock.json', 'r', encoding='UTF-8') as f:
    data_dict = json.load(f)
    stock_list = data_dict['stockList']
    for stock in stock_list:
        code = stock['code']
        try:
            with open(f'../spiders/股票数据/财务报表/CSV/{code}.csv', 'r', encoding='gbk') as fj:
                temp = next(fj)[0]
        except UnicodeDecodeError:
            error_code_dict.append(code)

with open('error_code_list.txt','w') as f:
    error_code_string = ','.join(error_code_dict)
    f.write(error_code_string)

print(len(error_code_dict))

# with open('./error_code_list.txt', 'r') as f:
#     error_code_list = f.read().split(',')
#     for code in error_code_list:
#         os.remove(f'../spiders/股票数据/财务报表/CSV/{code}.csv')