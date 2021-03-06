#!/bin/python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import json
import caculate as cc

historyData = []
result = dict()
lastDate = ''
updateStatusLocal = ()

def initData(updateStatusFunction):
    global updateStatusLocal
    global result
    global historyData
    global lastDate
    fp = open('result.json', 'r')
    result = json.load(fp)
    fp.close()
    fp = open('data.json', 'r')
    historyData = json.load(fp)
    fp.close()
    size = len(historyData)
    updateStatusLocal = updateStatusFunction
    if size == 0:
        if fetchHistory() == -1:
            return -1
        saveHistory()
        result = cc.countHeadTail(historyData)
        saveResult()
        lastDate = result['date']
    elif size > 0:
        if len(result) == 0 :
            result = cc.countHeadTail(historyData)
            saveResult()
            lastDate = result['date']
        else :
            lastDate = result['date']
            if lastDate != historyData[size-1]['date'] :
                '''TBD:sync data'''
        '''Update latest numbers'''
        if update() == -1:
            return 0
        saveHistory()
        result = cc.countHeadTail(historyData)
        saveResult()
        lastDate = result['date']
    return 1
        
def getResult():
    global result
    return result

def getHistory():
    global historyData
    return historyData

def getLatestDate():
    global lastDate
    return lastDate

def getMaxNumberOfPages():
    '''get total amount of pages first'''
    maxNumber = 0
    try:
        url = 'https://www.pilio.idv.tw/lto539/listbbk.asp?indexpage=1&orderby=old'
        res  = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        pages = soup.find_all('a', target='_self')
        urlStr = pages[3]['href']
        start = urlStr.find('indexpage=')
        if start >=0 :
            start = start + 10
            end = urlStr.find('&', start)
            if end > start :
                maxNumber = int(urlStr[start:end])
        print(maxNumber)
    except requests.exceptions.ConnectionError:
        updateStatus('????????????')
    except:
        updateStatus('?????????????????????')
        
    return maxNumber
    
def fetchHistory():
    global historyData
    historyData = []
    
    maxNumber = getMaxNumberOfPages()
    if maxNumber == 0:
        updateStatus('????????????????????????...')
        return -1
    
    updateStatus('?????????????????????...')
    try:
        for idx in range(1, maxNumber+1):
            url = f'https://www.pilio.idv.tw/lto539/listbbk.asp?indexpage={idx}&orderby=old'
            res  = requests.get(url)
            soup = BeautifulSoup(res.text,'html.parser')
            table = soup.find('table', border='1')
            trs = table.find_all('tr')
            trs.pop(0)
            for tr in trs:
                bs = tr.find_all('b', limit=3)
                bs.pop(0)
                dt = {}
                dt["date"] = bs[0].getText()
                dt["numbers"] = list(map(int, bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split(',')))
            historyData.append(dt)
        updateStatus('????????????????????????')
        return 1
    except requests.exceptions.ConnectionError:
        updateStatus('????????????')
        return -1
    except:
        updateStatus('?????????????????????')
        return -1

        
def update():
    global historyData
    global lastDate
    data = []
    found = False
    
    maxNumber = getMaxNumberOfPages()
    if maxNumber == 0:
        updateStatus('????????????????????????...')
        return -1
    
    updateStatus('???????????????...')
    try:
        for idx in range(1, maxNumber+1):
            url = f'https://www.pilio.idv.tw/lto539/listbbk.asp?indexpage={idx}'
            res  = requests.get(url)
            soup = BeautifulSoup(res.text,'html.parser')
            table = soup.find('table', border='1')
            trs = table.find_all('tr')
            trs.pop(0)
            for tr in trs:
                bs = tr.find_all('b', limit=3)
                bs.pop(0)
                if bs[0].getText() == lastDate:
                    found = True
                    break
                dt = {}
                dt["date"] = bs[0].getText()
                dt["numbers"] = list(map(int, bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split(',')))
                data.append(dt)
            if found == True :
                data.reverse()
                historyData.extend(data)
                updateStatus('????????????????????????')
                break;        
            idx = idx + 1
        return 1
    except requests.exceptions.ConnectionError:
        updateStatus('????????????')
        return -1
    except:
        updateStatus('?????????????????????')
        return -1


def saveHistory():
    updateStatus('?????????????????????')
    fp = open('data.json', 'w')
    global historyData
    fp.write(json.dumps(historyData))
    fp.flush()
    fp.close()
    updateStatus('????????????????????????')
    
def saveResult():
    updateStatus('?????????????????????')
    fp = open('result.json', 'w')
    global result
    fp.write(json.dumps(result))
    fp.flush()
    fp.close() 
    updateStatus('????????????????????????')
    
def updateStatus(status):
    updateStatusLocal(status)