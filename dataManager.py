#!/bin/python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import json
import caculate as cc

#updateStatusLocal = ()
class dataManager():
    
    historyData = []
    result = dict()
    lastDate = ''
    
    def initData(self):
        #global updateStatusLocal
        fp = open('result.json', 'r')
        self.result = json.load(fp)
        fp.close()
        fp = open('data.json', 'r')
        self.historyData = json.load(fp)
        fp.close()
        size = len(self.historyData)
        #updateStatusLocal = updateStatusFunction
        if size == 0:
            if self.fetchHistory() == -1:
                return -1
            self.saveHistory()
            self.result = cc.countHeadTail(self.historyData)
            self.saveResult()
            lastDate = self.result['date']
        elif size > 0:
            if len(self.result) == 0 :
                self.result = cc.countHeadTail(self.historyData)
                self.saveResult()
                self.lastDate = self.result['date']
            else :
                self.lastDate = self.result['date']
                if self.lastDate != self.historyData[size-1]['date'] :
                    '''TBD:sync data'''
            '''Update latest numbers'''
            if self.update() == -1:
                return 0
            self.saveHistory()
            self.result = cc.countHeadTail(self.historyData)
            self.saveResult()
            self.lastDate = self.result['date']
        return 1

    def getMaxNumberOfPages(self):
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
            #updateStatus('連線失敗')
            pass
        except:
            pass
            #updateStatus('未知的連線錯誤')

        return maxNumber

    def fetchHistory(self):
        self.historyData = []
    
        maxNumber = self.getMaxNumberOfPages()
        if maxNumber == 0:
            #updateStatus('抓取歷史獎號失敗...')
            return -1

        #updateStatus('抓取歷史獎號中...')
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
                    dt["numbers"] = list(map(int, bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split    (',')))
                    self.historyData.append(dt)
            #updateStatus('歷史獎號抓取完成')
            return 1
        except requests.exceptions.ConnectionError:
            #updateStatus('連線失敗')
            return -1
        except:
            #updateStatus('未知的連線錯誤')
            return -1


    def update(self):
        data = []
        found = False

        maxNumber = self.getMaxNumberOfPages()
        if maxNumber == 0:
            #updateStatus('更新歷史獎號失敗...')
            return -1

        #updateStatus('更新獎號中...')
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
                    if bs[0].getText() == self.lastDate:
                        found = True
                        break
                    dt = {}
                    dt["date"] = bs[0].getText()
                    dt["numbers"] = list(map(int, bs[1].getText().replace('\xa0\xa0', '\xa0,\xa0').replace('\xa0', '').split    (',')))
                    data.append(dt)
                if found == True :
                    data.reverse()
                    self.historyData.extend(data)
                    #updateStatus('歷史獎號更新完成')
                    break;        
                idx = idx + 1
            return 1
        except requests.exceptions.ConnectionError:
            #updateStatus('連線失敗')
            return -1
        except:
            #updateStatus('未知的連線錯誤')
            return -1


    def saveHistory(self):
        #updateStatus('歷史獎號儲存中')
        fp = open('data.json', 'w')
        fp.write(json.dumps(self.historyData))
        fp.flush()
        fp.close()
        #updateStatus('歷史獎號儲存完畢')

    def saveResult(self):
        #updateStatus('計算結果儲存中')
        fp = open('result.json', 'w')
        fp.write(json.dumps(self.result))
        fp.flush()
        fp.close() 
        #updateStatus('計算結果儲存完畢')

    def updateStatus(status):
    #updateStatusLocal(status)
        pass