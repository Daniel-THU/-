# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:13:40 2016

@author: liulei
"""

from nltk.corpus import gutenberg

allwords = gutenberg.words('shakespeare-hamlet.txt')

print len(allwords)

# 不重复的个数
len(set(allwords))

allwords.count('Hamlet')


A= set(allwords)
longwords = [w for w in A if len(w)>12]
print sorted(longwords)