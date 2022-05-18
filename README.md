# 金融项目--爬虫部分🕷

```shell
finance_project
├─.idea				# scrapy框架自带
|--relevent_json		# 完成辅助爬取
|--project
|  	|--README.md		
|  	|--scrapy.cfg		# 配置文件
|  	|--project
|		|--_pycache_ 	
|		|--automatic_crawl	# 自动化爬取脚本(bat/vbs)
|  		|--middlewares.py	# [中间件]设置随机User-Agent、代理
|  		|--pipelines.py		# [管道]处理数据、下载保存逻辑
|  		|--items.py			# 定义抓取数据结构
|  		|--settings.py		# 全局配置文件
|		|--spiders			# 🍉装载爬虫文件的目录
|			|--_pycache_
|			|--_init_.py	
|			|--money.py		# ->money.json
|			|--allStock.py	# ->all_stock.json
|			|--csvData.py	# ->财务报表.csv
|			|--pdfData.py	# ->财务报表.pdf
|			|--historical_trading_data.py	# ->历史交易数据
|			|--dailyPrice.py 	# ->实时股价-每日数据-年_月_日.json
|			|--股票数据		
|				|--财务报表
|					|--CSV
|					|--PDF
|				|--历史交易数据
|			|--实时股价
|				|--每日数据
|				|--数据
```

```PYTHON
# 如何爬取?
在finance_project/project/project/spiders位置打开命令行CMD
对不同爬虫执行不同命令行指令
```

#### 1.money.py

##### A股公司基本数据

```shell
scrapy crawl money -o moneyData.json
```

### 2.csvData.py

##### 年度财务报表.csv 

=> 保存路径 project--spiders--股票数据--财务报表--CSV

```shell
scrapy crawl csvData
```

#### 3.pdfData.py

##### 年度财务报表.pdf

=> 保存路径 project--spiders--股票数据--财务报表--PDF

```shell
scrapy crawl pdfData
```

#### 4.historical_trading_data.py

##### 历史交易数据.csv

=> 保存路径 project--spiders--股票数据--历史交易数据

```shell
scrapy crawl historical_trading_data 
```

#### 5.newPrice.py

##### 当前时刻所有股票价格

=> 保存路径 project--spiders--实时股价--数据

```shell
scrapy crawl newPrice
```

#### 6.dailyPrice.py

##### 当日所有股票每分钟价格

=> 保存路径 project--spiders--实时股价--每日数据

```shell
scrapy crawl dailyPrice
```

#### 7.allStock.py

```shell
scrapy crawl allStock -o all_stock.json
```

### 🏖网盘：爬取数据

链接：https://pan.baidu.com/s/1t7V7uf8ajDDdMgsJOhuDnw?pwd=0000 
提取码：0000 
--来自百度网盘超级会员V4的分享
