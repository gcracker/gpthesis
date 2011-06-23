#!/usr/bin/python
import sys
import os
import time
import datetime
import shutil
import subprocess

printLine = False
lineOut = False
outString = ""
paraArray = []
currFirstNum = -1
currArray = []
currCount = 0
interferPCount = 0
overLapCountArray = []
regionOverLap = []
curOverLapRegion = 0
overLapCount = 1
overLapHash = {}
lastOverLap = False

for line in sys.stdin:
   line = line.rstrip()
   line = line.strip()
   
   line = line.replace("Regions:", "Region ")

   if((-1 == line.find("Shrunk")) and(-1 == line.find("#Region")) and (-1 != line.find("Region"))):
      rLine = line[line.find("Region") + 6:line.find("->")]
      tLine = line[line.find("->")+2:]
      tLine = tLine.strip()
      tLine = tLine.rstrip()
      noDig = 1
      while ((noDig < len(tLine)) and
             (tLine[:noDig].isdigit())):
                noDig = noDig + 1
      if(noDig < len(tLine)):
         noDig = noDig - 1
         
      if(lastOverLap):
         tCount = overLapHash.get(int(tLine[:noDig]),0)
         overLapHash[int(tLine[:noDig])] = tCount + 1
      
      rLine = rLine.strip()
      rLine = rLine.rstrip()

      if (int(rLine) != curOverLapRegion):
         tRO = []
         for j in range(0, len(regionOverLap)):
            myCount = 1
            TlX = regionOverLap[j][0]
            BrX = regionOverLap[j][1]
            for i in range(0, len(overLapCountArray)):
               ar = overLapCountArray[i]
               if(((TlX >= ar[0]) and ((TlX <= ar[1]))) or
                  ((BrX >= ar[0]) and ((BrX <= ar[1]))) or 
                  ((TlX <= ar[0]) and ((BrX >= ar[0])))):
                  myCount = myCount + 1
                  ar[2] = ar[2] + 1
                  overLapCountArray[i] = ar
            tRO.append([TlX,BrX,myCount,regionOverLap[j][3]])

         rCount = overLapHash.get(int(rLine),0)
         overLapHash[int(rLine)] = rCount + overLapCount
         overLapCount = 1
         curOverLapRegion = int(rLine)
         if(0 < len(tRO)):
            overLapCountArray = overLapCountArray + tRO
         regionOverLap = []

   if(-1 != line.find("Overlap")):
      overLapLine = line[line.find("Overlap")+8:]
      overLapLine = overLapLine.rstrip()
      overLapLine = overLapLine.strip()
      TlLine = overLapLine.split(",")[0]
      BrLine = overLapLine.split(",")[1]
      
      TlLine = TlLine.replace("TL", "")
      TlLine = TlLine.rstrip()
      TlLine = TlLine.strip()

      BrLine = BrLine.replace("BR", "")
      BrLine = BrLine.rstrip()
      BrLine = BrLine.strip()
      
      TlX = int(TlLine.split(" ")[0].replace("X:",""))
      BrX = int(BrLine.split(" ")[0].replace("X:",""))

      if((0 != TlX) and ((0 != BrX))):
        
         lastOverLap = True
         overLapCount = overLapCount + 1

         tmpRA = []
         for i in range(0, len(regionOverLap)):
            ar = regionOverLap[i]
            if(((TlX >= ar[0]) and ((TlX <= ar[1]))) or
               ((BrX >= ar[0]) and ((BrX <= ar[1]))) or 
               ((TlX <= ar[0]) and ((BrX >= ar[0])))):

               if(TlX > ar[0]):
                  TlX = ar[0]
               if(BrX < ar[1]):
                  BrX = ar[1]
            else:
               tmpRA.append(ar)
         regionOverLap = tmpRA        
         regionOverLap.append([TlX,BrX,1,curOverLapRegion])
         
      else:
         lastOverLap = False

   
#    if(-1 != line.find("Shrunk Regions:")):
#       line = line.replace("Shrunk Regions:", "")
#       lineSplit = line.split(":")
#       lineSize = int(lineSplit[1])
#       if(lineSplit[0] != currFirstNum):
#          print str(currFirstNum) + ":" + str(interferPCount)
#          interferPCount = 0

#          currArray.append(str(currCount))
#          if(0 < len(currArray)):
#             paraArray.append(currArray)
#          currArray = [lineSplit[0]]
#          currFirstNum = lineSplit[0]
#          currCount = 0
#       if (0 < lineSize):
#          lineSplit = line.split("->")
#          currArray.append(lineSplit[1].split(",")[0])
#          currCount = currCount + int(lineSplit[1].split(",")[1].split(":")[1])
#    if(-1 != line.find("Interference Removal Forward Slice Set:")):
#       lineSplit = line.split(":")
#       lineSize = int(lineSplit[1])
#       if (0 < lineSize):
#          interferPCount = interferPCount + 1

# paraArray.sort(lambda a,b : cmp(int(a[len(a)-1]),int(b[len(b)-1])))
# for a in paraArray:
#    tempString = ""
#    for c in a:
#       if "\"" == tempString:
#          tempString = tempString + c
#       else:
#          tempString = tempString + " " + c
#    tempString = tempString
#    print tempString
print overLapCountArray

maxCount = 1
for i in range(0, len(overLapCountArray)):
   ar = overLapCountArray[i]
   if(maxCount < ar[2]):
      maxCount = ar[2]
print maxCount
