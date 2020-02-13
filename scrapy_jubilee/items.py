# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyJubileeItem(scrapy.Item):
    # define the fields for your item here like:
    constellation_name  = scrapy.Field() # type varchar 3
    overall_score 		= scrapy.Field() # type int
    overall_description = scrapy.Field() # type text
    love_score 			= scrapy.Field() # type int
    love_description 	= scrapy.Field() # type text
    work_score 			= scrapy.Field() # type int
    work_description 	= scrapy.Field() # type text
    money_score 		= scrapy.Field() # type int
    money_description 	= scrapy.Field() # type text
    date 				= scrapy.Field() # type date