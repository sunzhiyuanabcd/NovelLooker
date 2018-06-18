#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time :2018/6/17/017 19:48
#!@Author :zhiyuansun
#!@File :.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def result(request):
    return render(request,'result.html')

def error(request):
    return render(request,'result.html')