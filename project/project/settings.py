# Scrapy settings for project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'project'

SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'project (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # False表示不遵守robotstxt协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'project.middlewares.ProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'project.middlewares.RandomUserAgentMiddleware': 300,
    # 'project.middlewares.RandomProxyMiddleware': 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'project.pipelines.csvDataPipeline': 1,
    # 'project.pipelines.pdfDataPipeline': 2,
    # 'project.pipelines.historicalTradingDataPipeline': 3, # 爬虫特有pipeline在所属爬虫中定义
}

FILES_STORE = '股票数据'


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

FEED_EXPORT_ENCODING = 'utf-8'
COOKIES_ENABLED = False # 禁用cookies

# #减少请求并发数量
# CONCURRENT_REQUESTS = 8 # Scrapy下载器发送的最大并发请求数(默认:16)
# CONCURRENT_REQUESTS_PER_DOMAIN = 4 # Scrapy针对一个域名的最大并发请求书(默认:8)
# # CONCURRENT_REQUESTS_PER_IP = 0
# #设置请求间隔
# DOWNLOAD_DELAY = 0.5 # 默认:0(单位秒)


# 代理:
# proxy: 'http://' + 'xxx.xxx.xx:xxx'
# PROXIES = ['...','...',...]

# feed export保存文件路劲
