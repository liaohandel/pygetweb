#!/usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import time


import json
import copy

import requests
from bs4 import BeautifulSoup

#from bs4 import BeautifulSoup 
soup={}


def chkhtml(filename):
    global soup
    with open(filename, "r", encoding="utf8") as fp:
        soup = BeautifulSoup(fp, "lxml")
    
    #tag_div = soup.find(id="real_1")
    #tag_c1 = tag_div.find(class_="bd scrl")
    #tag_c2 = tag_c1.find(class_="idxtab3")
    #tag_span = tag_c2.find("tr")
    #print(tag_span.string)

    tag_div = soup.find(id="real_1")
    tag_div2 = tag_div.find(attrs={"class":"idxtab3"})
    tag_table = tag_div2.find("table")
    #tag_tbody = tag_table.find("tbody")
    tag_tr = tag_table.find("tr")
    print(tag_tr)
    tag_tr = tag_table.find("tr")
    print(tag_tr)
    for i in tag_table:
        print("===============")
        print(i)
    #print(tag_div2.string)
    #print(tag_div2)
    #print(tag_tr)
    #print(tag_tbody)

    # 搜尋<a>標籤
    #tag_a = soup.find("a") 
    #print(tag_a.string)
    # 呼叫多次find()方法
    #tag_p = soup.find(name="p")
    #tag_a = tag_p.find(name="a")
    #print(tag_p.a.string)
    #print(tag_a.string)


if __name__ == '__main__':
    if len(sys.argv)>1:
        chkhtml(sys.argv[1])
    else:
        print(">>not input filename.html ...")