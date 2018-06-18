#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time :2018/6/17/017 18:59
#!@Author :zhiyuansun
#!@File :.py

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env