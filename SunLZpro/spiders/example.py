# -*- coding: utf-8 -*-
import scrapy
from SunLZpro.items import SunlzproItem
from time import sleep
class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://yglz.tousu.hebnews.cn/sssb-9.html']

    def __init__(self):
        self.page = 9
        self.url = "http://yglz.tousu.hebnews.cn/sssb-%d.html"

    def parse(self, response):


        div_list = response.xpath('//*[@id="divList"]/div[@class="listcon"]')
        for span in div_list:
            Company = span.xpath('.//span[1]/p/a/text()').extract_first()
            Classify = span.xpath('.//span[2]/p/text()').extract_first()
            theme = span.xpath('.//span[3]/p/a/@title').extract_first()
            start_time = span.xpath('.//span[4]/p/text()').extract_first()
            end_time = span.xpath('.//span[5]/p/text()').extract_first()
            state = span.xpath('.//span[6]/p/text()').extract_first()
            item = SunlzproItem()
            item["Company"] = Company
            item["Classify"] = Classify
            item["theme"] = theme
            item["start_time"] = start_time
            item["end_time"] = end_time
            item["state"] = state

            yield item
        self.page += 1
        # if self.page % 10 == 0:
        #     sleep(2)
        if self.page < 100:
            next_url = format(self.url % self.page)
            yield scrapy.Request(url=next_url, callback=self.parse)