from scrapy import cmdline
import os


os.chdir('../spiders')

cmd_str = 'scrapy crawl dailyPrice'
cmdline.execute(cmd_str.split())





