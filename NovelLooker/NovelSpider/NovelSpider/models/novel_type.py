#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time :2018/6/17/017 8:30
#!@Author :zhiyuansun
#!@File :.py
from elasticsearch_dsl import DocType,Date,Keyword,Text,Integer,analyzer
from elasticsearch_dsl.connections import connections

#创建连接器
connections.create_connection(hosts=["localhost"])

#创建数据Model类，继承DocType，定义各个字段的数据类型
class NovelType(DocType):
    novel_name=Text(analyzer='ik_max_word')
    novel_cover_url=Keyword()
    novel_author=Text(analyzer='ik_max_word')
    novel_intro=Text(analyzer='ik_max_word')
    novel_tags=Text(analyzer='ik_max_word')
    novel_chapters_url=Keyword()
    crawl_time=Date()

    class Meta:
        index="novels"
        doc_type="novel"

if __name__=="__main__":
    #调用init方法建立映射mappings
    NovelType.init()

