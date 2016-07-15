# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:07:16 2016

@author: liulei
"""

'''
时间序列
'''

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start , today)
fields = ['date', 'open', 'close', 'high','low','volume']

list1=[]

for i in range(0, len(quotes)):
    x= date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)

quotesdf = pd.DataFrame(quotes, index = list1, columns=fields)
quotesdf = quotesdf.drop(['date'], axis=1)

#print quotesdf



'''
统计近一年每个月的股票开盘天数
'''
import time 

listtemp = []
for i in range(0, len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],'%Y-%m-%d')
    listtemp.append(temp.tm_mon)
print listtemp

tempdf = quotesdf.copy()
tempdf['month']= listtemp

print tempdf['month'].value_counts()



'''
Groupby 函数
'''

tempdf.groupby('month').count().month




'''
近一年每个月的总成交量
'''
tempdf.groupby('month').sum().volume



'''
微软公司（MSFT）2014年第一季度股票收盘价的平均值
'''
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo_ochl('MSFT', start, today)
attributes=['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)

list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)

quotesdfMS.index = list
quotesdfMS = quotesdfMS.drop(['date'], axis = 1)
list = []

quotesdfMS14 = quotesdfMS['14/01/01':'14/12/31']
for i in range(0, len(quotesdfMS14)):
    list.append(int(quotesdfMS14.index[i][3:5])) #get month just like '02'

quotesdfMS14['month'] = list
print quotesdfMS14.groupby('month').mean().close