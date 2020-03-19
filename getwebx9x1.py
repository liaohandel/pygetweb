#!/usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import os
import time

from selenium import webdriver
from bs4 import BeautifulSoup
#import requests
from bs4 import BeautifulSoup
webdriver = webdriver.Chrome("./chromedriver")

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
    #weblink = "http://traderoom.cnyes.com/tse/quote2FB.aspx?code="+stock_sn
    weblink = "https://stock.pchome.com.tw/stock/sto0/ock3/sid"+stock_sn+".html"

    #r = requests.get(weblink,timeout=10)
    #r.encoding = "utf-8"
    #soup = BeautifulSoup(r.text, "lxml")


    webdriver.implicitly_wait(10)
    webdriver.get(weblink)
    print(webdriver.title)
    soup = BeautifulSoup(webdriver.page_source, "lxml")
    #fp = open("index.html", "w", encoding="utf8")
    #fp.write(soup.prettify())
    #print("寫入檔案index.html...")
    #fp.close()
    #webdriver.quit()

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

