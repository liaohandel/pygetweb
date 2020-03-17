#!/usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import os
import time

import requests
from bs4 import BeautifulSoup


def chk_datepath():
    nowget =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    yy = nowget[0:4]
    mm = nowget[5:7]
    mydate = "day"+yy+"M"+mm
    os.chdir("\py3_prj\pyweb\stock_data")# dir path select 
    ll=os.listdir()
    if mydate not in ll:
        os.mkdir(mydate)

    return mydate

def load_stockweb(stock_sn,datepath):
    nowget =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #stock_sn="3231"
    weblink = "http://traderoom.cnyes.com/tse/quote2FB.aspx?code="+stock_sn
    r = requests.get(weblink,timeout=10)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")

    os.chdir("\\py3_prj\\pyweb\\stock_data\\"+datepath)
    sfilename = "stock"+stock_sn+"d"+nowget[0:10]+".html"
    fp = open(sfilename , "w", encoding="utf8")
    fp.write(soup.prettify())
    #print(nowget[0:10])
    print("寫入檔案"+sfilename)
    fp.close()

if __name__ == '__main__':
    if len(sys.argv)>1:
        sspath = chk_datepath()
        print(sspath)
        #print(type(sspath))
        #load_stockweb("3231",sspath)
        sn=sys.argv[1]
        load_stockweb(sn,sspath)

