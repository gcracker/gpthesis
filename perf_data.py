#!/usr/bin/python
import sys
import os
import time
import datetime
import shutil
import subprocess

g_homeDir = os.path.expanduser("~")

g_dataSearchDirs = [os.getcwd() + "/raw_data/"]

g_outDir = os.getcwd() + "/data/"

print "Writing data to: " + g_outDir

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

            fileLine = textFH.readline()
            fileLine = fileLine.strip();
            fileLine = fileLine.rstrip();
            
            if (-1 != firstLine.find("Performance Tests")):
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
               
               naiveCount = -1
               naivePerf = -1.0
               interferCount = -1
               interferPerf = -1.0
               parallelCountNaive = 0
               parallelCountInterfer = 0

               lineArray = textFH.readlines()
               lineCount = 0
               currentRegionIDs = []
               currentRegionXs = []
               naiveRegionParallel = []
               interferRegionParallel = []

               while (lineCount < len(lineArray)):

                  line = lineArray[lineCount]
                  line = line.rstrip()
                  line = line.strip()

                  if(False == jobMetrics.get("OPTI", False)):
                     if (-1 != line.find("Naive Count:")):
                        lineParts = line.split(":")
                        naiveCount = int(lineParts[1].rstrip().strip().rstrip("%"))
                        jobMetrics["naiveCount"] = naiveCount
                        jobMetrics["nFile"] = textfile

                     if (-1 != line.find("Naive Performance Gain:")):
                        lineParts = line.split(":")
                        naivePerf = float(lineParts[1].rstrip().strip().rstrip("%"))
                        jobMetrics["naivePerf"] = naivePerf
                        jobMetrics["nFile"] = textfile

                  if (-1 != line.find("Simple Interference Count:")):
                     lineParts = line.split(":")
                     interferCount = int(lineParts[1].rstrip().strip().rstrip("%"))
                     jobMetrics["interferCount"] = interferCount
                     jobMetrics["intFile"] = textfile

                  if (-1 != line.find("Simple Interference Performance Gain:")):
                     lineParts = line.split(":")
                     interferPerf = float(lineParts[1].rstrip().strip().rstrip("%"))
                     jobMetrics["interferPerf"] = interferPerf
                     jobMetrics["intFile"] = textfile

                  if ((-1 != line.find("Regions:")) and
                      (-1 == line.find("Shrunk"))):
                     regionLine = line.replace("Regions:","")
                     currentRegionIDs = regionLine[:regionLine.find(",")].split("->")
                     tlX = int(regionLine[regionLine.find("X:")+2:regionLine.find("Y:")].rstrip().strip())
                     brX = int(regionLine[regionLine.rfind("X:")+2:regionLine.rfind("Y:")].rstrip().strip())
                     currentRegionXs = [tlX, brX]

                  if (-1 != line.find("Shrunk Regions:")):
                     naiveCount = int(line[line.rfind(":")+1:].rstrip().strip())
                     naiveThreadCount = 2
                     newNaiveRegionParallel = []
                     if (0 < naiveCount):
                        for regions in naiveRegionParallel:
                           if (((regions[0] > currentRegionXs[0]) and
                                (regions[0] < currentRegionXs[1])) or
                               (((regions[1] < currentRegionXs[1]) and
                                 (regions[1] > currentRegionXs[0])))):
                              regions[2] = regions[2] + 1
                              naiveThreadCount = naiveThreadCount + 1
                           newNaiveRegionParallel.append(regions)
                        newNaiveRegionParallel.append([currentRegionXs[0], currentRegionXs[1], naiveThreadCount])
                        naiveRegionParallel = newNaiveRegionParallel

                  if (-1 != line.find("#RegionID,")):

                     parallelType = line[line.find(",") + 1:]
                     parallelCount = 0

                     lineCount = lineCount + 1
                     line = lineArray[lineCount]
                     line = line.rstrip()
                     line = line.strip()

                     while(((lineCount+1) < len(lineArray)) and 
                           (0 < len(lineArray[lineCount+1])) and
                           (lineArray[lineCount+1][0].isdigit())):
                        lineCount = lineCount + 1
                        line = lineArray[lineCount]
                        line = line.rstrip()
                        line = line.strip()

                        tmpParallelCount = int(line.split(",")[1]) + 1
                        if (tmpParallelCount > parallelCount):
                           parallelCount = tmpParallelCount

                     if (-1 != parallelType.find("Interfer")):
                        parallelCountInterfer = parallelCount
                        jobMetrics["parallelCountInterfer"] = parallelCountInterfer
                        jobMetrics["inpFile"] = textfile
                     elif (-1 != parallelType.find("Naive")):
                        if(False == jobMetrics.get("OPTI", False)):
                           parallelCountNaive = parallelCount
                           jobMetrics["parallelCountNaive"] = parallelCountNaive
                           jobMetrics["npFile"] = textfile

                  lineCount = lineCount + 1                  

               if(False == jobMetrics.get("OPTI", False)):
                  topNaiveCount = 0
                  for regions in naiveRegionParallel:
                     if topNaiveCount < regions[2]:
                        topNaiveCount = regions[2]
                  jobMetrics["parallelCountNaiveTxt"] = topNaiveCount

               if (-1 != firstLine.find("Optimal Performance Tests")):
                  if (0 < jobMetrics.get("naivePerf", -1)):
                     jobMetrics["OPTI"] = True

               jobHashOpti[opti] = jobMetrics
               g_perfOut[jobHashName] = jobHashOpti

            textFH.close()

jobOptiList = ["O0", "O2"]

for jobOpti in jobOptiList:

   naivePerfOut = g_outDir + "tlpNaivePerf" + jobOpti + ".data"
   npFH = open(naivePerfOut, "w")
   npFH.write("#Benchmark,Naive TLP\n")
   sortList = g_perfOut.items()
   sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   for jobName,jobOptiHash in sortList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      jmNum = jobMetrics.get("naivePerf", None)
      print "Naive " + jobName + " " + jobOpti + " File:" + jobMetrics.get("nFile","")
      if None != jmNum:
         npFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   npFH.close()

   interferPerfOut = g_outDir + "tlpInterferPerf" + jobOpti + ".data"
   inFH = open(interferPerfOut, "w")
   inFH.write("#Benchmark,TLP W/O Interference\n")
   sortList = g_perfOut.items()
   sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   for jobName,jobOptiHash in sortList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      jmNum = jobMetrics.get("interferPerf", None)
      print "Interfer " + jobName + " " + jobOpti + " File:" + jobMetrics.get("intFile","")
      if None != jmNum:
         inFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   inFH.close()

   perfOut = g_outDir + "tlpPerf" + jobOpti + ".data"
   perFH = open(perfOut, "w")
   perFH.write("#Benchmark,Naive TLP,TLP W/O Interference\n")
   sortList = g_perfOut.items()
   sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   for jobName,jobOptiHash in sortList:
      jobMetrics = jobOptiHash.get(jobOpti,{})
      jmNumA = jobMetrics.get("naivePerf", None)
      jmNumB = jobMetrics.get("interferPerf", None)
      if ((None != jmNumA) and (None != jmNumB)):
         perFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNumA) + "," + str(jmNumB) + "\n")
   perFH.close()

   # naiveParallelOut = g_outDir + "tlpNaiveParallel" + jobOpti + ".data"
   # nParFH = open(naiveParallelOut, "w")
   # nParFH.write("#Benchmark,Max Threads Naive\n")
   # sortList = g_perfOut.items()
   # sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   # for jobName,jobOptiHash in sortList:
   #    jobMetrics = jobOptiHash.get(jobOpti,{})
   #    jmNum = jobMetrics.get("parallelCountNaive", None)
   #    print "parallelNaive " + jobName + " " + jobOpti + " File:" + jobMetrics.get("npFile","")
   #    if None != jmNum:
   #       nParFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   # nParFH.close()

   # interferParallelOut = g_outDir + "tlpInterferParallel" + jobOpti + ".data"
   # nInterferFH = open(interferParallelOut, "w")
   # nInterferFH.write("#Benchmark,Max Threads W/O Interference\n")
   # sortList = g_perfOut.items()
   # sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   # for jobName,jobOptiHash in sortList:
   #    jobMetrics = jobOptiHash.get(jobOpti,{})
   #    jmNum = jobMetrics.get("parallelCountInterfer", None)
   #    print "parallelInter " + jobName + " " + jobOpti + " File:" + jobMetrics.get("inpFile","")
   #    if None != jmNum:
   #       nInterferFH.write(jobName[:3] + "." + jobName[3:] + "," + str(jmNum) + "\n")
   # nInterferFH.close()

   # parallelOut = g_outDir + "tlpParallel" + jobOpti + ".data"
   # nTlpFH = open(parallelOut, "w")
   # nTlpFH.write("#Benchmark,Max Threads Naive,Max Threads W/O Interference\n")
   # sortList = g_perfOut.items()
   # sortList.sort(lambda a,b : cmp(int(a[0][:3]),int(b[0][:3])))
   # for jobName,jobOptiHash in sortList:
   #    jobMetrics = jobOptiHash.get(jobOpti,{})
   #    jmNumA = jobMetrics.get("parallelCountNaive", None)
   #    jmNumB = jobMetrics.get("parallelCountInterfer", None)
   #    if ((None != jmNumA) and (None != jmNumB)):
   #       nTlpFH.write(jobName[:3] + "." + jobName[3:]  + "," + str(jmNumA) + "," + str(jmNumB) + "\n")
   # nTlpFH.close()
