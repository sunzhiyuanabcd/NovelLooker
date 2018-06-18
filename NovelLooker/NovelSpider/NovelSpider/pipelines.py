# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from NovelLooker.NovelSpider.NovelSpider.items import NovelspiderItem
class NovelspiderPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        item.save_to_elasticsearch()
        return item

    def spider_closed(self, spider):
        pass

