#!/bin/python3
#coding:utf-8

import tkinter as tk
from tkinter import ttk
import dataManager as dm

#import caculate as cc

def updateStatus(status):
    statusLabel['text'] = status

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)
    
def startProcess():
    refreshBtn['state'] = tk.DISABLED
    ret = dm.initData(updateStatus)
    if ret != -1:
        result = dm.getResult()
        datas = dm.getHistory()

        idx = 0
        for data in datas:
            treeview.insert('', idx, values=(data['date'], data['numbers'][0], data['numbers'][1], data['numbers'][2], data['numbers'][3], data['numbers'][4]))
            idx = idx + 1

        v_total_head0['text'] = result['head'][0]
        v_total_head1['text'] = result['head'][1]
        v_total_head2['text'] = result['head'][2]
        v_total_head3['text'] = result['head'][3]
        v_avg_head0['text'] = truncate(result['head'][0]/9 , 3)
        v_avg_head1['text'] = truncate(result['head'][1]/10, 3)
        v_avg_head2['text'] = truncate(result['head'][2]/10, 3)
        v_avg_head3['text'] = truncate(result['head'][3]/10, 3)

        v_total_tail0['text'] = result['tail'][0]
        v_total_tail1['text'] = result['tail'][1]
        v_total_tail2['text'] = result['tail'][2]
        v_total_tail3['text'] = result['tail'][3]
        v_total_tail4['text'] = result['tail'][4]
        v_total_tail5['text'] = result['tail'][5]
        v_total_tail6['text'] = result['tail'][6]
        v_total_tail7['text'] = result['tail'][7]
        v_total_tail8['text'] = result['tail'][8]
        v_total_tail9['text'] = result['tail'][9]
        v_avg_tail0['text'] = truncate(result['tail'][0]/3, 3)
        v_avg_tail1['text'] = truncate(result['tail'][1]/4, 3)
        v_avg_tail2['text'] = truncate(result['tail'][2]/4, 3)
        v_avg_tail3['text'] = truncate(result['tail'][3]/4, 3)
        v_avg_tail4['text'] = truncate(result['tail'][4]/4, 3)
        v_avg_tail5['text'] = truncate(result['tail'][5]/4, 3)
        v_avg_tail6['text'] = truncate(result['tail'][6]/4, 3)
        v_avg_tail7['text'] = truncate(result['tail'][7]/4, 3)
        v_avg_tail8['text'] = truncate(result['tail'][8]/4, 3)
        v_avg_tail9['text'] = truncate(result['tail'][9]/4, 3)

        lastDateLable['text'] = f'????????????:{dm.getLatestDate()}'
        if ret == 1:
            updateStatus('??????')
        #else:
        #    refreshBtn['state'] = tk.NORMAL
    else:
        print('Something wrong')
        #refreshBtn['state'] = tk.NORMAL
    refreshBtn['state'] = tk.NORMAL
    
version = "Version 1.0.0"    
w_width = 640
w_height = 480
status_height = 28
version_width = 100
content_height = w_height - status_height -28
   
root = tk.Tk()

root.title("??????539")
root.geometry(f"{w_width}x{w_height}+100+100")
root.resizable(False, False)


tabCtl = ttk.Notebook(root, width=w_width, height=content_height)
headTailTab = tk.Frame(tabCtl)
tabCtl.add(headTailTab, text='???/?????????')

lastDateLable = tk.Label(headTailTab, width=16)
lastDateLable.grid(column=0, row=0, padx=5, sticky="W", columnspan=8)

tk.Label(headTailTab, text='').grid(column=1, row=1, sticky="E")
head0 = tk.Label(headTailTab, text='0???:')
head1 = tk.Label(headTailTab, text='1???:')
head2 = tk.Label(headTailTab, text='2???:')
head3 = tk.Label(headTailTab, text='3???:')
head0.grid(column=1, row=2, sticky="E")
head1.grid(column=1, row=3, sticky="E")
head2.grid(column=1, row=4, sticky="E")
head3.grid(column=1, row=5, sticky="E")

tk.Label(headTailTab, text='?????????').grid(column=2, row=1)
v_total_head0 = tk.Label(headTailTab, text='0')
v_total_head1 = tk.Label(headTailTab, text='0')
v_total_head2 = tk.Label(headTailTab, text='0')
v_total_head3 = tk.Label(headTailTab, text='0')
v_total_head0.grid(column=2, row=2, sticky="W")
v_total_head1.grid(column=2, row=3, sticky="W")
v_total_head2.grid(column=2, row=4, sticky="W")
v_total_head3.grid(column=2, row=5, sticky="W")

tk.Label(headTailTab, text='????????????').grid(column=3, row=1)
v_avg_head0 = tk.Label(headTailTab, text='0')
v_avg_head1 = tk.Label(headTailTab, text='0')
v_avg_head2 = tk.Label(headTailTab, text='0')
v_avg_head3 = tk.Label(headTailTab, text='0')
v_avg_head0.grid(column=3, row=2, sticky="W")
v_avg_head1.grid(column=3, row=3, sticky="W")
v_avg_head2.grid(column=3, row=4, sticky="W")
v_avg_head3.grid(column=3, row=5, sticky="W")

tk.Label(headTailTab, width=10).grid(column=4, row=1)

tk.Label(headTailTab, text='').grid(column=5, row=1, sticky="E")
tail0 = tk.Label(headTailTab, text='0???:')
tail1 = tk.Label(headTailTab, text='1???:')
tail2 = tk.Label(headTailTab, text='2???:')
tail3 = tk.Label(headTailTab, text='3???:')
tail4 = tk.Label(headTailTab, text='4???:')
tail5 = tk.Label(headTailTab, text='5???:')
tail6 = tk.Label(headTailTab, text='6???:')
tail7 = tk.Label(headTailTab, text='7???:')
tail8 = tk.Label(headTailTab, text='8???:')
tail9 = tk.Label(headTailTab, text='9???:')
tail0.grid(column=5, row=2, sticky="E")
tail1.grid(column=5, row=3, sticky="E")
tail2.grid(column=5, row=4, sticky="E")
tail3.grid(column=5, row=5, sticky="E")
tail4.grid(column=5, row=5, sticky="E")
tail5.grid(column=5, row=6, sticky="E")
tail6.grid(column=5, row=7, sticky="E")
tail7.grid(column=5, row=8, sticky="E")
tail8.grid(column=5, row=9, sticky="E")
tail9.grid(column=5, row=10, sticky="E")

tk.Label(headTailTab, text='?????????').grid(column=6, row=1)
v_total_tail0 = tk.Label(headTailTab, text='0')
v_total_tail1 = tk.Label(headTailTab, text='0')
v_total_tail2 = tk.Label(headTailTab, text='0')
v_total_tail3 = tk.Label(headTailTab, text='0')
v_total_tail4 = tk.Label(headTailTab, text='0')
v_total_tail5 = tk.Label(headTailTab, text='0')
v_total_tail6 = tk.Label(headTailTab, text='0')
v_total_tail7 = tk.Label(headTailTab, text='0')
v_total_tail8 = tk.Label(headTailTab, text='0')
v_total_tail9 = tk.Label(headTailTab, text='0')
v_total_tail0.grid(column=6, row=2, sticky="W")
v_total_tail1.grid(column=6, row=3, sticky="W")
v_total_tail2.grid(column=6, row=4, sticky="W")
v_total_tail3.grid(column=6, row=5, sticky="W")
v_total_tail4.grid(column=6, row=5, sticky="W")
v_total_tail5.grid(column=6, row=6, sticky="W")
v_total_tail6.grid(column=6, row=7, sticky="W")
v_total_tail7.grid(column=6, row=8, sticky="W")
v_total_tail8.grid(column=6, row=9, sticky="W")
v_total_tail9.grid(column=6, row=10, sticky="W")

tk.Label(headTailTab, text='????????????').grid(column=7, row=1)
v_avg_tail0 = tk.Label(headTailTab, text='0')
v_avg_tail1 = tk.Label(headTailTab, text='0')
v_avg_tail2 = tk.Label(headTailTab, text='0')
v_avg_tail3 = tk.Label(headTailTab, text='0')
v_avg_tail4 = tk.Label(headTailTab, text='0')
v_avg_tail5 = tk.Label(headTailTab, text='0')
v_avg_tail6 = tk.Label(headTailTab, text='0')
v_avg_tail7 = tk.Label(headTailTab, text='0')
v_avg_tail8 = tk.Label(headTailTab, text='0')
v_avg_tail9 = tk.Label(headTailTab, text='0')
v_avg_tail0.grid(column=7, row=2, sticky="W")
v_avg_tail1.grid(column=7, row=3, sticky="W")
v_avg_tail2.grid(column=7, row=4, sticky="W")
v_avg_tail3.grid(column=7, row=5, sticky="W")
v_avg_tail4.grid(column=7, row=5, sticky="W")
v_avg_tail5.grid(column=7, row=6, sticky="W")
v_avg_tail6.grid(column=7, row=7, sticky="W")
v_avg_tail7.grid(column=7, row=8, sticky="W")
v_avg_tail8.grid(column=7, row=9, sticky="W")
v_avg_tail9.grid(column=7, row=10, sticky="W")

tk.Label(headTailTab, width=10).grid(column=8, row=1)

refreshBtn = tk.Button(headTailTab, text='????????????', command=startProcess, state=tk.DISABLED)
refreshBtn.grid(column=9, row=1, rowspan=2, columnspan=2)

#??????????????????
historyTab = tk.Frame(tabCtl)
tabCtl.add(historyTab, text='????????????')

scrollBar = tk.Scrollbar(historyTab)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

columns = ('????????????', '??????1', '??????2', '??????3', '??????4', '??????5')
treeview = ttk.Treeview(historyTab, height=18, show="headings", columns=columns, yscrollcommand=scrollBar.set)

treeview.column('????????????', width=100, anchor='center')
treeview.column('??????1', width=50, anchor='center')
treeview.column('??????2', width=50, anchor='center')
treeview.column('??????3', width=50, anchor='center')
treeview.column('??????4', width=50, anchor='center')
treeview.column('??????5', width=50, anchor='center')

treeview.heading('????????????', text='????????????')
treeview.heading('??????1',    text='??????1')
treeview.heading('??????2',    text='??????2')
treeview.heading('??????3',    text='??????3')
treeview.heading('??????4',    text='??????4')
treeview.heading('??????5',    text='??????5')

treeview.pack(side='left', fill='both')
scrollBar.config(command=treeview.yview)

tabCtl.pack()

#statusFrame = tk.Frame(root, width=w_width, height=status_height, padx=1, pady=1, bg="#e0e0e0")
#statusFrame.pack()
statusLabel = tk.Label(root, text="?????????", anchor="w", bg='#e0e0e0')
versionLabel = tk.Label(root, text=version, bg='#e0e0e0')
statusLabel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=1, pady=1, ipadx=5)
versionLabel.pack(side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1, ipadx=5)

root.after(100, startProcess)
root.mainloop()
