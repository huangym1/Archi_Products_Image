# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArchiproductsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_1_url = scrapy.Field()
    detail_2_url = scrapy.Field()
    detail_3_url = scrapy.Field()
    image_url = scrapy.Field()
    next_url = scrapy.Field()
