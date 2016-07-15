# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:14:16 2016

@author: liulei
"""

'''
输出2-100之内的素数
'''

from math import sqrt

#i=2
#
#while  i <= 100:
#    j=2    
#    k = sqrt(i)
#
#    while j <= k:
#        if i%j == 0:
#            break
#        j+=1
#    if j > k:
#        print i
#    
#    i+=1
#    

#for i in range(2,101):
#    
#    k = int(sqrt(i))
#    flag=1
#    for j in range(2, k+1):
#        
#        if i%j==0:
#            flag =0            
#            break
#        
#    if(flag):
#        print i
    

# 3函数方法

def isPrime(x):
    if x==1:
        return False
    k= int (sqrt(x))
    for j in range(2, k+1):
        if x%j==0:
            return False
    return True



for i in range(2, 101):
    if isPrime(i):
        print i
        
