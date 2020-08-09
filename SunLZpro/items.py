# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunlzproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Company = scrapy.Field()
    Classify = scrapy.Field()
    theme = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    state = scrapy.Field()
