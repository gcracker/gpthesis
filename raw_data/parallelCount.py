#!/usr/bin/python
import sys
import os
import time
import datetime

nCounts = {}
iCounts = {}
regA = ""
regB = ""

for line in sys.stdin:
    line = line.strip()
    line = line.rstrip()
    if -1 != line.find("Region"):
        nCnt = int(line [line.rfind(":")+1:])
        if 0 < nCnt:
            regs = line[line.find("Region")+6:line.find("Naive Size:")]
            regA = regs[:regs.find("->")]
            regB = regs[regs.find("->")+2:]
            regA = regA.strip()
            regA = regA.rstrip()
            regB = regB.strip()
            regB = regB.rstrip()
            
            nTemp = nCounts.get(regA,0)
            nTemp = nTemp + 1
            nCounts[regA] = nTemp
            nTemp = nCounts.get(regB,0)
            nTemp = nTemp + 1
            nCounts[regB] = nTemp
    if -1 != line.find("Interference Removal Forward Slice Set:"):
        iCnt = int(line [line.rfind(":")+1:])
        if 0 < iCnt:
            iTemp = iCounts.get(regA,0)
            iTemp = iTemp + 1
            iCounts[regA] = iTemp
            iTemp = iCounts.get(regB,0)
            iTemp = iTemp + 1
            iCounts[regB] = iTemp

print "#RegionID,Naive"
for reg,nCnt in sorted(nCounts.items(), key=lambda entry: int(entry[0])):
    print reg + "," + str(nCnt)

print "#RegionID,Interfer"
for reg,iCnt in sorted(iCounts.items(), key=lambda entry:int(entry[0])):
    print reg + "," + str(iCnt)
