# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from NovelLooker.NovelSpider.NovelSpider.models.novel_type import NovelType

class NovelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名
    novelname=scrapy.Field()
    #小说封面url
    novelcover=scrapy.Field()
    #小说作者
    novelauthor=scrapy.Field()
    #小说标签
    noveltags=scrapy.Field()
    #小说引入语
    novelintro=scrapy.Field()
    #小说总字数
    #noveltotalchars=scrapy.Field()
    #小说总章节数
    #noveltotalchapters=scrapy.Field()
    #小说章节分布所在的URL
    novelchapters=scrapy.Field()
    novelcrawltime=scrapy.Field()

    def save_to_elasticsearch(self):
        novel=NovelType()
        novel.novel_name=self['novelname']
        novel.novel_author=self['novelauthor']
        novel.novel_cover_url=self['novelcover']
        novel.novel_intro=self['novelintro']
        novel.novel_tags=self['noveltags']
        novel.novel_chapters_url=self['novelchapters']
        novel.crawl_time=self['novelcrawltime']

        novel.save()

