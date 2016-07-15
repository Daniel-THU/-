# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:53:44 2016

@author: liulei
"""

sum = 0 
i=1

while i<=5:
    sum += i
    i += 1
    if i==2:
        continue
    print sum