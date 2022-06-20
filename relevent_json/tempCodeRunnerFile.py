with open(filename) as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         itemDict = {}
#         print(line)
#         # print(type(line))
#         itemDict['date'] = line['日期']
#         itemDict['start'] = line['开盘价']
#         itemDict['end'] = line['收盘价']
#         itemDict['highest'] = line['最高价']
#         itemDict['lowest'] = line['最低价']
#         itemDict['up_down'] = line['涨跌幅']
#         itemDict['exchange'] = line['换手率']
#         itemDict['price'] = line['成交金额']
#         jsonList.append(itemDict)

# jsonFileName = filename[:4] 
# with open()