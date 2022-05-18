# 数据说明

#### 🕷<font color='green'>该项目所需数据已""全部!""完成爬取,并列举如下👇</font>

### 1.stock.json

##### 所有股票的<font color='red'>""最基础""</font>数据[股票代码、股票中文简称]

##### <font color='purple'>=> 用于遍历所有股票</font>

```C++
orgId: 组织id -- 巨潮资讯网站url所需参数
category: 股票类型 -- A股
code: 6位股票代码
pinyin: 股票拼音
zwjc: 股票中文简称
```

### 2.moneyData.json

##### 股票(上市公司)的<font color='purple'>公司信息</font>

```C++
code
category
组织形式
地域
中文简称
办公地址
公司全称
公司电话
英文名称
公司电子邮箱
注册资本
董事长
员工人数
董事会秘书
法人代表
董秘电话
总经理
董秘传真
信息披露网址
信息披露报纸名称
主营业务
经营范围
公司沿革
```

### 3.all_stock.json

```python
code
category: 上证A股 深证A股 北证A股
cur_name: 当前A股名字
category_index: sh sz bj
```

### 4.股票数据

- #### 财务报表

  - ##### <font color='red'>CSV </font>

  - **PDF** -- **弃**(可以但没必要)

- #### 历史交易数据

  - ##### <font color='red'>CSV</font>

### 5.股票数据

- ##### <font color='red'>"每日数据"文件夹</font> 

  - ##### <font color='red'>json文件: 每日某股票每分钟数据</font>

  

