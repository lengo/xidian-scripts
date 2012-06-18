#!/usr/bin/env python
# coding=utf-8

import requests
import hashlib
import re
import time
from lxml import html

BASE_URL = "http://202.117.122.8/patroninfo"

LOGIN_URL = BASE_URL
POST_URL = BASE_URL

CARD_NO = "cord number here"
PIN = "your pin"

def login():
    s = requests.session()
#    login_page = s.get(LOGIN_URL)
    
    data = {
            "code": CARD_NO,
            "pin": PIN
            }
    res = s.post(POST_URL, data)
    m = re.search('patroninfo(.*)/items', res.text)
    userinfo = m.group(1)
    ITEM_URL = BASE_URL + str(userinfo) + "/items"
#    print ITEM_URL
    return [s, ITEM_URL]

def print_borrowinfo(s, ITEM_URL):
    r = s.get(ITEM_URL)
    doc = html.document_fromstring(r.text)
    trs = doc.xpath("//tr[@class='patFuncEntry']") 
    print "=========借阅情况==========="
    for tr in trs:
        td = tr.findall('td')
        for i in [1, 3]:
            print td[i].text_content().strip().encode('utf-8')
        print
    print "==========END=========="

if __name__ == '__main__':
    [s, ITEM_URL]  = login()
    print_borrowinfo(s, ITEM_URL)
