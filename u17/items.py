# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class U17Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comic_id = scrapy.Field()
    name = scrapy.Field()
    cover = scrapy.Field()
    category = scrapy.Field()


# class U17DetailItem(scrapy.Item):
#     name = scrapy.Field()