#!/usr/bin/env python3
#Alec Snyder
#allonsy
#code to help solve crosswords

import re
import sys



#read in database:
words=[]

fil=open("dict.db", "r")
for word in fil:
    word=word[:len(word)-1]
    words.append(word)

for arg in sys.argv:
    if(arg=="./crossword.py"):
        continue
    print("Results for word: "+arg)
    pat=re.compile('^'+arg+'$')
    for wd in words:
        mat=pat.match(wd)
        if(mat):
            print(wd)
    print("================")


