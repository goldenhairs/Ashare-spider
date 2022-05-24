# Scrapy使用要点:

### 1.给定url下载文件:

##### <font color='purple'>使用Scrapy自带的FilesPipeline</font>

##### 参考Scrapy文档:[下载和处理文件和图像 — Scrapy 2.5.0 文档 (osgeo.cn)](https://www.osgeo.cn/scrapy/topics/media-pipeline.html?highlight=filespipeline#scrapy.pipelines.files.FilesPipeline)

```python
# pipelines.py
from scrapy.pipelines.files import FilesPipeline
```

##### ①pipelines.py

##### 编写pipeline继承FilesPipeline,重定义<font color='green'>get_media_request</font>和<font color='green'>file_path</font>方法:

```python
class xxxPipeline(FilesPipeline):
	def get_media_request(self, item, info):
        # 构造request对象 -- 修饰请求头
		yield Request(item['file_urls'], meta={'name': item['name']})
    def file_path(self, request, response=None, info=None, *, item=None):
        # 重定义文件名和下载路径
        name = request.meta['name']
        return f'/财务报表/CSV/{name}.csv' # 文件的相对路径
```

##### ②items.py

##### 定义items,保证必须包含<font color='green'>file_urls</font>字段和<font color='green'>files</font>字段,可以添加任意其他字段

```python
class xxxItem(scrapy.Item):
	name = scrapy.Field() 
	file_urls = scrapy.Field() # 目标文件url -- 应该是列表
	files = scrapy.Field() # 下载文件时,该字段会被结果填充,包含下载文件的信息的dict列表
```

##### ③settings.py

##### 定义FILES_STORE字段

```python
FILES_STORE = '/path/to/valid/dir' # 文件下载相对路径 -- 相对于执行路径 
```

##### ④spider

##### Spider类中定义custom_settings对管道赋予权重,也可写入settings全局配置中

```python
class xxxSpider(scrapy.Spider):
	custom_settings = {
	'ITEM_PIPELINES':{
		'project.pipelines.xxxPipelines': 1,
		}
	}
```

### 2.导出json文件(不用FEED EXPORT)

##### 使用项目导出器 <font color='purple'>JsonItemExporter</font>

##### 参考Scrapy文档:[条目导出器 — Scrapy 2.5.0 文档 (osgeo.cn)](https://www.osgeo.cn/scrapy/topics/exporters.html?highlight=jsonitemexporter#)

```python
from scrapy.exporters import JsonItemExporter
```

##### 通过调用三个方法:<font color='green'>start_exporting(),export_item(),finish_exporting()</font>

```python
class xxxPipeline:
	def open_spider(self, spider):
		self.fp = open('文件', 'wb') # 通过open函数打开文件并返回文件对象 -- 该文件就是目标存储文件
		self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8', indent=4)
		self.exporter.start_exporting()
	def close_spider(self, spider):
		self.exporter.finish_exporting()
		self.fp.close()
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
```

