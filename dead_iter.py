#!/usr/bin/python
import sys
import os
import time
import datetime
import shutil
import subprocess

g_homeDir = os.path.expanduser("~")

g_dataSearchDirs = [os.getcwd() + "/raw_data/deathSlice/"]

g_outDir = os.getcwd() + "/data/"

g_perfOut = {}

for searchDir in g_dataSearchDirs:
   for dirname, dirnames, filenames in os.walk(searchDir):

      for filename in filenames:
         if(filename.endswith(".txt")):
            textfile = os.path.join(dirname, filename)
            textFH = open(textfile, "r")
            firstLine = textFH.readline()
            firstLine = firstLine.strip();
            firstLine = firstLine.rstrip();

            fileLine = None
            while None == fileLine:               
               fileLine = textFH.readline()
               fileLine = fileLine.strip()
               fileLine = fileLine.rstrip()
               if(-1 == fileLine.find("Using")):
                  fileLine = None
            
            if (-1 != firstLine.find("Dead Code Iter Test")):
               
               fileLine = fileLine.split("/")[len(fileLine.split("/"))-1]
               jobNameParts = fileLine.replace(".txt","").replace(".dd","").replace(".slr","").split("_")
               jobName = jobNameParts[0]
               opti = ""
               test = ""
               for part in jobNameParts:
                  if (-1 != part.find("O")):
                     opti = part
                  elif ((-1 != part.find("test")) and
                        (-1 == part.find("perftest"))):
                     test = part

               jobHashName = jobName
               jobHashOpti = g_perfOut.get(jobHashName, {})
               jobMetrics = jobHashOpti.get(opti, {})
               
               lineArray = textFH.readlines()
               lineCount = 0
               deadDiff = []
               deadFinal = 0
               deadTotal = 0

               while (lineCount < len(lineArray)):

                  line = lineArray[lineCount]
                  line = line.rstrip()
                  line = line.strip()

                  if (-1 != line.find("DdDiff:")):
                     lineParts = line.split(":")
                     deadDiff.append(int(lineParts[1].rstrip().strip()))
                     deadTotal = deadTotal + int(lineParts[1].rstrip().strip())

                  if (-1 != line.find("DdFinalSize:")):
                     lineParts = line.split(":")
                     deadFinal = int(lineParts[1].rstrip().strip())

                  lineCount = lineCount + 1

               deadCountList = [deadFinal]
               deadCount = deadFinal
               deadDiff.reverse()
               
               for count in deadDiff:
                  deadCount = deadCount + count
                  deadCountList.append(deadCount)
               deadDiff.reverse()
               deadCountList.reverse()
 
               jobMetrics["FINAL"] = deadFinal
               jobMetrics["DIFF"] = deadDiff

               if(0 != deadFinal):
                  jobMetrics["DEADTOTALPERCENT"] = int(float(deadTotal) / (float(deadTotal + deadFinal)) * 100)

               jobMetrics["DEADTOTAL"] = deadTotal
               jobMetrics["COUNTLIST"] = deadCountList

               jobHashOpti[opti] = jobMetrics
               g_perfOut[jobHashName] = jobHashOpti

            textFH.close()

jobOptiList = ["O0", "O2"]
sortJobList = g_perfOut.items()
sortJobList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))

for jobName,jobOptiHash in sortJobList:
   dcrOut = g_outDir + jobName + "DeadCodeRemoved.data"
   fh = open(dcrOut, "w")
   headerLine = "#Slice Iteration"
   jobLists = {}
   jobString = []
   maxCount = 0
   for jobOpti in jobOptiList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      diffList = jobMetrics.get("DIFF", None)
      if None != diffList:
         if(len(diffList) > maxCount):
            maxCount = len(diffList)
         jobLists[jobOpti] = diffList
   for opti,jobList in jobLists.items():
      headerLine = headerLine + "," + opti
      stringCount = 0
      while (stringCount < maxCount):
         curString = ""
         if stringCount >= len(jobString):
            curString = str(stringCount)
         else:
            curString = jobString[stringCount]
         if stringCount < len(jobList):
            curString = curString + " " + str(jobList[stringCount])
         else:
            curString = curString + " 0"
         if stringCount < len(jobString):
            jobString[stringCount] = curString
         else:
            jobString.append(curString)
         stringCount = stringCount + 1
   fh.write(headerLine + "\n")
   for line in jobString:
      fh.write(line + "\n")
   fh.close()

for jobOpti in jobOptiList:
   deadOut = g_outDir + "deadCodeTotal" + jobOpti + ".data"
   inFH = open(deadOut, "w")
   inFH.write("#Benchmark,Irrelevant Dependence Count\n")
   sortList = g_perfOut.items()
   sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   for jobName,jobOptiHash in sortList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      jmNum = jobMetrics.get("DEADTOTAL", None)
      if None != jmNum:
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   inFH.close()

for jobOpti in jobOptiList:
   deadOut = g_outDir + "deadCodeTotalPercent" + jobOpti + ".data"
   inFH = open(deadOut, "w")
   inFH.write("#Benchmark,Irrelevant Dependence Percent\n")
   sortList = g_perfOut.items()
   sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   for jobName,jobOptiHash in sortList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      jmNum = jobMetrics.get("DEADTOTALPERCENT", None)
      if None != jmNum:
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   inFH.close()


for jobName,jobOptiHash in sortJobList:
   headerLine = "#Slice Iteration, O0 O2 Diff"
   jobListO0 = []
   jobListO2 = []
   jobString = []
   minCount = 100000
   for jobOpti in jobOptiList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      diffList = jobMetrics.get("DIFF", None)
      if None != diffList:
         if(len(diffList) < minCount):
            minCount = len(diffList)
         if "O0" == jobOpti:
            jobListO0 = diffList
         else:
            jobListO2 = diffList
   dcrOut = g_outDir + jobName + "DeadCodeDiffRemoved.data"
   fh = open(dcrOut, "w")
   fh.write(headerLine + "\n")
   if ((0 < len(jobListO0)) and (0 < len(jobListO2))):
      stringCount = 0
      while (stringCount < minCount):
         curString = ""
         if stringCount >= len(jobString):
            curString = str(stringCount)
         else:
            curString = jobString[stringCount]

         curString = curString + " " + str(jobListO0[stringCount] - jobListO2[stringCount])
         
         if stringCount < len(jobString):
            jobString[stringCount] = curString
         else:
            jobString.append(curString)
         stringCount = stringCount + 1

      for line in jobString:
         fh.write(line + "\n")
   else:
      fh.write("0 0\n")
      fh.write("1 1\n")
   fh.close()

sortList = g_perfOut.items()
sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
deadOut = g_outDir + "deadCodeDiffTotal.data"
inFH = open(deadOut, "w")
inFH.write("#Benchmark,Irrelevant Dependence Count Diff\n")
for jobName,jobOptiHash in sortList:
   jobMetricsO0 = jobOptiHash.get("O0",{})
   jobMetricsO2 = jobOptiHash.get("O2",{})
   if((0 < len(jobMetricsO0)) and (0 < len(jobMetricsO2))):
      jmNumO0 = jobMetricsO0.get("DEADTOTAL", 0)
      jmNumO2 = jobMetricsO2.get("DEADTOTAL", 0)
      if ((0 != jmNumO0) and (0 != jmNumO2)):
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNumO0 - jmNumO2) + "\n")
   else:
      inFH.write(jobName[:3] + "." + jobName[3:] + ",0\n")
inFH.close()


sortList = g_perfOut.items()
sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
deadOut = g_outDir + "deadCodeDiffTotalPercent.data"
inFH = open(deadOut, "w")
inFH.write("#Benchmark,Irrelevant Dependence Percent Diff\n")
for jobName,jobOptiHash in sortList:
   jobMetricsO0 = jobOptiHash.get("O0",{})
   jobMetricsO2 = jobOptiHash.get("O2",{})
   if((0 < len(jobMetricsO0)) and (0 < len(jobMetricsO2))):
      jmNumO0 = jobMetricsO0.get("DEADTOTALPERCENT", 0)
      jmNumO2 = jobMetricsO2.get("DEADTOTALPERCENT", 0)
      if ((0 != jmNumO0) and (0 != jmNumO2)):
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNumO0 - jmNumO2) + "\n")
   else:
      inFH.write(jobName[:3] + "." + jobName[3:] + ",0\n")
inFH.close()

sortList = g_perfOut.items()
sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
deadOut = g_outDir + "deadCodeBothTotal.data"
inFH = open(deadOut, "w")
inFH.write("#Benchmark,Irrelevant Dependence Count O0, Irrelevant Dependence Count O2\n")
for jobName,jobOptiHash in sortList:
   jobMetricsO0 = jobOptiHash.get("O0",{})
   jobMetricsO2 = jobOptiHash.get("O2",{})
   if((0 < len(jobMetricsO0)) and (0 < len(jobMetricsO2))):
      jmNumO0 = jobMetricsO0.get("DEADTOTAL", 0)
      jmNumO2 = jobMetricsO2.get("DEADTOTAL", 0)
      if ((0 != jmNumO0) and (0 != jmNumO2)):
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNumO0) + "," + str(jmNumO2) + "\n")
   else:
      inFH.write(jobName[:3] + "." + jobName[3:] + ",0,0\n")
inFH.close()

sortList = g_perfOut.items()
sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
deadOut = g_outDir + "deadCodeBothTotalPercent.data"
inFH = open(deadOut, "w")
inFH.write("#Benchmark,Irrelevant Dependence Percent O0, Irrelevant Dependence Percent O2\n")
for jobName,jobOptiHash in sortList:
   jobMetricsO0 = jobOptiHash.get("O0",{})
   jobMetricsO2 = jobOptiHash.get("O2",{})
   if((0 < len(jobMetricsO0)) and (0 < len(jobMetricsO2))):
      jmNumO0 = jobMetricsO0.get("DEADTOTALPERCENT", 0)
      jmNumO2 = jobMetricsO2.get("DEADTOTALPERCENT", 0)
      if ((0 != jmNumO0) and (0 != jmNumO2)):
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNumO0) + "," + str(jmNumO2) + "\n")
   else:
      inFH.write(jobName[:3] + "." + jobName[3:] + ",0,0\n")
inFH.close()
