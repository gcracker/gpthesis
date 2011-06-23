#!/usr/bin/python

import os, sys, re, string, operator, types, math, random,re, types
from collections import deque

outHash = {}

def addToTrie(word,wHash):
    if(1 < len(word)):
        tHash = wHash.get(word[0],{})
        wHash[word[0]] = addToTrie(word[1:],tHash)
    else:
        wHash[word[0]] = {}
    return wHash

def getDiveBreadth(wHash, word, breadth):

    if(15 < breadth):
        print word + "..."
    elif (0 == len(wHash)):
        print word        
    else:
        for w,wH in wHash.items():
            if((w != "_") and (w != "~") 
               and (w != "<") and (w != ">")
               and (w != ":")):            
                getDiveBreadth(wH,word+w,breadth + len(wH))
            else:
                getDiveBreadth(wH,word+w,breadth)

for line in sys.stdin:
    line = line.rstrip()
    line = line.strip()
    if(80 < len(line)):
        line = line[:76] + "..."

    outHash = addToTrie(line,outHash)

getDiveBreadth(outHash, "", 0)  

