# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:23:10 2016

@author: liulei
"""

'''
猜数字游戏
'''

import random 

x = random.randint(0, 10)

go = 'y'

while (go == 'y'):
    print  'please input one number between 0-10'
    digit = int(raw_input())
    
    if digit == x:
        print 'Bingo'
        break
    elif x > digit:
        print "too small"
    else:
        print "too large" 
    print 'if you dont want to continue, input n, or input y'
    go = raw_input('go or not > ')

else:
    print 'goodbye'
    
    