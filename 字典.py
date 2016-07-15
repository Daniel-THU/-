# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:44:38 2016

@author: liulei
"""

'''
字典
'''
from pandas import Series
sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])

#sa.equals(sc)
#sb.equals(sa)



import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])


dict1 = {'xiaoyun':88888,'xiaohong':5555555,'xiaoteng':11111,'xiaoyi':12341234,'xiaoyang':1212121}

#name = raw_input("Please input the name:")
#print dict1[name]

listV = dict1.values()
listK = dict1.keys()

print  "Who has the nice QQ number?"
for i in range(0,len(listV)):
    if listV[i]< 100000:
        print listK[i]
        
        
        
        