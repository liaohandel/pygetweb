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

import getwebx6

jstocklist={}

def expto_temp(filename):
    global jstocklist

    os.chdir(".\\stock_note")
    ll=os.listdir()
    print(ll)

    jfile = open(filename,'r',encoding="utf-8")
    jstocklist = json.loads(jfile.read())
    #jstr=jfile.readlines
    jfile.close()

    for i in jstocklist["[stocksn]"]:
        print(i)
        for j in jstocklist["[stocksn]"][i]:
            print(i+"-"+j)



if __name__ == '__main__':
    #print(len(sys.argv))
    if len(sys.argv)>1:
        print(">>load stock_list to json buffer ...")
        expto_temp(sys.argv[1])

        sspath = getwebx6.chk_datepath()
        print(">>save path = "+sspath)
        for i in jstocklist["[stocksn]"]:
            if len(i) > 0:
                for j in jstocklist["[stocksn]"][i]:
                    getwebx6.load_stockweb(j,sspath)
                    print(">>load data"+j)
                    time.sleep(3)

    else:
        print(">>not load json ...")
