#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time :2018/6/17/017 6:59
#!@Author :zhiyuansun
#!@File :.py
from scrapy import cmdline

name='qidian_novel'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())