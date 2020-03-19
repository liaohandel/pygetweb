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
tablist=[]

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
    #tag_table = tag_table1.find("tbody")
    #tag_tbody = tag_table.find("tbody")
    tag_tr = tag_table.find_all("tr")
    print(len(tag_tr))
    print(len(tag_tr[1]))

    #print(tag_tr[1])
    #jj=0
    #for j in tag_tr[1]:
    #    print("===="+str(jj)+"#",len(j))
    #    if len(j)>1:
    #        for k in j:
    #            print("######")
    #            print(k)
    #    else:
    #        print(j)
    #        print("==>",j.string.strip())
    #    jj=jj+1

    for i in tag_tr:
        lll=[]
        x1 = i.find_all("td")
        for j in x1:
            if len(j)<2:
                #print(j.string.strip())
                lll.append(j.string.strip())
        #print(lll)
        if len(lll)>4:
            stime = lll[0]
            sbuy = lll[1]
            ssell = lll[2]
            sfind = lll[3]
            scount = lll[4]
            if (float(sfind)==float(sbuy)):
                sflag=0
            else:
                sflag=1
            sitem = "%s,%s,%s,%s,%s,%s"%(stime,sbuy,ssell,sfind,scount,sflag)
            tablist.append(sitem)

    print(tablist)
    #tag_lt = tag_tr[1].find_all("td",class_="lt")
    #print("=======")
    #print(tag_lt)
    #tag_price = tag_tr[1].find_all("td",class_="price")
    #print("=======")
    #print(tag_price)
    #tag_rt = tag_tr[1].find_all("td",class_="rt")
    #print("=======")
    #print(tag_rt)

    #tag_tr = tag_table.find("tr")
    #print(tag_tr)
    #for i in tag_table:
    #    print("===============")
    #    print(i)
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