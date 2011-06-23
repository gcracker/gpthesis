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
outFH = None

if 1 < len(sys.argv):
   outFH = open(sys.argv[1], "w")

for line in sys.stdin:

   line = line.rstrip()
   line = line.strip()
   
   if(("" == line) and 
      (True == lineOut)):
      lineOut = False
      if(None == outFH):
         print outString + "\n"
      else:
         outFH.write(outString + "\n\n")
      outString = ""
   elif(-1 != line.find("begin{document}")):
      printLine = True
   elif(-1 != line.find("end{document}")):
      printLine = False
   elif(-1 != line.find("begin{figure}")):
      printLine = False
   elif(-1 != line.find("end{figure}")):
      printLine = True
   elif(-1 != line.find("\\appendix")):
      printLine = False
   elif(-1 != line.find("begin{enumerate}")):
      printLine = printLine
   elif(-1 != line.find("end{enumerate}")):
      printLine = printLine
   elif(-1 != line.find("begin{abstract}")):
      printLine = printLine
   elif(-1 != line.find("\\abstract")):
      printLine = True
   elif(-1 != line.find("end{abstract}")):
      printLine = printLine
   elif(-1 != line.find("\\label")):
      printLine = printLine
   elif(True == printLine):
      if(-1 != line.find("\\item")):
         line = line.strip("\\item") + "\n"
      elif(-1 != line.find("\\section")):
         line = line.strip("\\section{")
         line = line.rstrip("}") + "\n"
         line = "SECTION: " + line
      elif(-1 != line.find("\\chapter")):
         line = line.strip("\\chapter{")
         line = line.rstrip("}") + "\n"
         line = "CHAPTER: " + line
      if("" != line):
         if (("" != outString) and 
             (" " != line[0])):
            outString = outString + " " 
         
         outString = outString + line
         lineOut = True
