# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SunlzproPipeline(object):

    def __init__(self):
        self.fp = None
        # 重写父类方法

    def open_spider(self, spider):
        print('我是open_spider(),我只会在爬虫开始的时候执行一次')
        self.fp = open('sun.csv', 'a+', newline="",encoding='gbk')
        self.writer = csv.writer(self.fp)
        self.writer.writerow(('受理单位','分类','主题','受理时间','办结时间','办理状态'))
    def close_spider(self, spider):
        print('我是close_spider(),我只会在爬虫结束的时候执行一次')
        self.fp.close()

        # 用来接收item对象

    def process_item(self, item, spider):

        # 将item存储到文本文件
        self.writer.writerow((item['Company'],item['Classify'],item["theme"],item["start_time"],item["end_time"],item["state"]))

        return item