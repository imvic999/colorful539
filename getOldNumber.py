#!/bin/python3
#coding:utf-8

import requests
#import re
from bs4 import BeautifulSoup
import json

data = []
for idx in range(1, 154):
#for idx in range(1, 2):
    url = f'https://www.pilio.idv.tw/lto539/listbbk.asp?indexpage={idx}&orderby=old'
    res  = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    
    table = soup.find('table', border='1')
    #print(table)
    
    trs = table.find_all('tr')
    trs.pop(0)
    #print(trs)
    for tr in trs:
        bs = tr.find_all('b', limit=3)
        bs.pop(0)
        #print(bs[0].getText())
        #numbers = bs[1].getText()
        #numbers = numbers.replace('\xa0\xa0', '\xa0,\xa0')
        numbers = bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '')
        #print(bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', ''))
        #numbers = bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split(',')
        #print(numbers)
        dt = {}
        dt["date"] = bs[0].getText()
        dt["numbers"] = list(map(int, bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split(',')))
        data.append(dt)
        
fp = open('data.json', 'w')
fp.write(json.dumps(data))
fp.flush()
fp.close()

#fp2 = open('data.json', 'r')
_data = json.load(open('data.json', 'r'))
#print(_data[1]["date"])
#print(_data[1]["numbers"])
#fp2.close()
#for table in soup.select('table'):
#   match = re.search()
print("Done!!!")



