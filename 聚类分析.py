# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:30:25 2016

@author: liulei
"""

'''
聚类分析
'''

from pylab import *
from scipy.cluster.vq import *

list1 = [88, 74, 96, 85]
list2 = [92,99, 95, 94]
list3 = [91, 87, 99, 95]
list4 = [78, 99, 97, 81]
list5 = [88, 78, 98, 84]
list6 = [100, 95, 100, 92]

#data = vstack((list1,list2,list3,list4,list5,list6))
#centroids,_ = kmeans(data,2)
#result, _ = vq(data, centroids)


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1)
y = np.sin(4 * np.pi* x) * np.exp(-5 * x)

plt.plot(x, y, 'o')
plt.show() 

