from scrapy import cmdline
import os

# os.chdir('E:\\finance_project\\project\\project\\spiders')
os.chdir('../spiders')




cmd_str = 'scrapy crawl tenDays'
cmdline.execute(cmd_str.split())