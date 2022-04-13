#!/bin/python3
#coding:utf-8

def countHeadTail(datas):
    if len(datas) == 0 :
        return
    count = [0 for n in range(40)]
    for data in datas:
        for number in data['numbers']:
            count[number] = count[number]+1

    hTotal = [0 for n in range(4)]
    tTotal = [0 for n in range(10)]
    for j in range(0, 4):
        for i in range(0, 10):
            idx = j*10+i
            hTotal[j] = hTotal[j] + count[idx]
            tTotal[i] = tTotal[i] + count[idx]

    result = {}
    result['date'] = datas[len(datas)-1]['date']
    result['all'] = count
    result['head'] = hTotal
    result['tail'] = tTotal

    return result