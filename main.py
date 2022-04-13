#!/bin/python3
#coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import dataManager as dm

#import caculate as cc

def updateStatus(status):
    statusLabel['text'] = status

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

'''    
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

        lastDateLable['text'] = f'更新獎號:{dm.getLatestDate()}'
        if ret == 1:
            updateStatus('完成')
        #else:
        #    refreshBtn['state'] = tk.NORMAL
    else:
        print('Something wrong')
        #refreshBtn['state'] = tk.NORMAL
    refreshBtn['state'] = tk.NORMAL
'''
Builder.load_string("""
<WelcomeScreen>:
    BoxLayout:
        Label:
            text: 'Updating'

<HeadTailScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to welcome'
            on_press: root.manager.current = 'welcome'
            
<HistoryScreen>:
    BoxLayout:
        Label:
            text: '更新中'
            
<AboutScreen>:
    BoxLayout:
        Label:
            text: '版本: 1.0.0'
""")

    
class WelcomeScreen(Screen):
    pass
class HeadTailScreen(Screen):
    pass
class HistoryScreen(Screen):
    pass
class AboutScreen(Screen):
    pass

class Colorful539(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HeadTailScreen(name='head_tail'))
        sm.add_widget(HistoryScreen(name='hirstoy'))
        sm.add_widget(AboutScreen(name='about'))
        return sm
 
    def startProcess():
        ret = dm.initData()
        if ret != -1:
            result = dm.getResult()
            datas = dm.getHistory()

            '''
            idx = 0
            for data in datas:
                treeview.insert('', idx, values=(data['date'], data['numbers'][0], data['numbers'][1], data['numbers'][2], data['numbers'][3], data['numbers'][4]))
                idx = idx + 1
            '''
            if ret == 1:
                updateStatus('完成')
        else:
            print('Something wrong')
            
Colorful539().run()

'''
version = "Version 1.0.0"    
w_width = 640
w_height = 480
status_height = 28
version_width = 100
content_height = w_height - status_height -28
   
root = tk.Tk()

root.title("今彩539")
root.geometry(f"{w_width}x{w_height}+100+100")
root.resizable(False, False)


tabCtl = ttk.Notebook(root, width=w_width, height=content_height)
headTailTab = tk.Frame(tabCtl)
tabCtl.add(headTailTab, text='頭/尾統計')

lastDateLable = tk.Label(headTailTab, width=16)
lastDateLable.grid(column=0, row=0, padx=5, sticky="W", columnspan=8)

tk.Label(headTailTab, text='').grid(column=1, row=1, sticky="E")
head0 = tk.Label(headTailTab, text='0頭:')
head1 = tk.Label(headTailTab, text='1頭:')
head2 = tk.Label(headTailTab, text='2頭:')
head3 = tk.Label(headTailTab, text='3頭:')
head0.grid(column=1, row=2, sticky="E")
head1.grid(column=1, row=3, sticky="E")
head2.grid(column=1, row=4, sticky="E")
head3.grid(column=1, row=5, sticky="E")

tk.Label(headTailTab, text='總次數').grid(column=2, row=1)
v_total_head0 = tk.Label(headTailTab, text='0')
v_total_head1 = tk.Label(headTailTab, text='0')
v_total_head2 = tk.Label(headTailTab, text='0')
v_total_head3 = tk.Label(headTailTab, text='0')
v_total_head0.grid(column=2, row=2, sticky="W")
v_total_head1.grid(column=2, row=3, sticky="W")
v_total_head2.grid(column=2, row=4, sticky="W")
v_total_head3.grid(column=2, row=5, sticky="W")

tk.Label(headTailTab, text='平均次數').grid(column=3, row=1)
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
tail0 = tk.Label(headTailTab, text='0尾:')
tail1 = tk.Label(headTailTab, text='1尾:')
tail2 = tk.Label(headTailTab, text='2尾:')
tail3 = tk.Label(headTailTab, text='3尾:')
tail4 = tk.Label(headTailTab, text='4尾:')
tail5 = tk.Label(headTailTab, text='5尾:')
tail6 = tk.Label(headTailTab, text='6尾:')
tail7 = tk.Label(headTailTab, text='7尾:')
tail8 = tk.Label(headTailTab, text='8尾:')
tail9 = tk.Label(headTailTab, text='9尾:')
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

tk.Label(headTailTab, text='總次數').grid(column=6, row=1)
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

tk.Label(headTailTab, text='平均次數').grid(column=7, row=1)
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

refreshBtn = tk.Button(headTailTab, text='重新整理', command=startProcess, state=tk.DISABLED)
refreshBtn.grid(column=9, row=1, rowspan=2, columnspan=2)

#歷史獎號頁面
historyTab = tk.Frame(tabCtl)
tabCtl.add(historyTab, text='歷史獎號')

scrollBar = tk.Scrollbar(historyTab)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

columns = ('開獎日期', '獎號1', '獎號2', '獎號3', '獎號4', '獎號5')
treeview = ttk.Treeview(historyTab, height=18, show="headings", columns=columns, yscrollcommand=scrollBar.set)

treeview.column('開獎日期', width=100, anchor='center')
treeview.column('獎號1', width=50, anchor='center')
treeview.column('獎號2', width=50, anchor='center')
treeview.column('獎號3', width=50, anchor='center')
treeview.column('獎號4', width=50, anchor='center')
treeview.column('獎號5', width=50, anchor='center')

treeview.heading('開獎日期', text='開獎日期')
treeview.heading('獎號1',    text='獎號1')
treeview.heading('獎號2',    text='獎號2')
treeview.heading('獎號3',    text='獎號3')
treeview.heading('獎號4',    text='獎號4')
treeview.heading('獎號5',    text='獎號5')

treeview.pack(side='left', fill='both')
scrollBar.config(command=treeview.yview)

tabCtl.pack()

#statusFrame = tk.Frame(root, width=w_width, height=status_height, padx=1, pady=1, bg="#e0e0e0")
#statusFrame.pack()
statusLabel = tk.Label(root, text="啟動中", anchor="w", bg='#e0e0e0')
versionLabel = tk.Label(root, text=version, bg='#e0e0e0')
statusLabel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=1, pady=1, ipadx=5)
versionLabel.pack(side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1, ipadx=5)

root.after(100, startProcess)
root.mainloop()
'''