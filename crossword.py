#!/usr/bin/env python3
#Alec Snyder
#allonsy
#code to help solve crosswords

import re
import sys

def remPunc(word):
    ret=""
    for c in word:
        if(c.isalpha()):
            ret+=c.lower()
        elif(c.isnumeric()):
            ret+=c.lower()
    return ret


#read in database:
words=[]

fil=open("dict.db", "r")
for word in fil:
    words.append(word.lower())

for arg in sys.argv:
    if(arg=="./crossword.py"):
        continue
    print("Results for word: "+arg)
    pat=re.compile('^'+arg+'$')
    for wd in words:
        wd=remPunc(wd)
        mat=pat.match(wd)
        if(mat):
            print(wd)
    print("================")


