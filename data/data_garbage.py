#!/usr/bin/python
import sys
import re


if len(sys.argv) < 3:	
        print "I need more cowbell"
else:	

        finalHash = {}
        finalLine = ""

        inputfile = open(sys.argv[1], 'r')

        count = 1;

        for line in inputfile:

                if (line[0].isdigit()):
                        
                        totalGarbage = 0
                        finalLine = ""
                        substrs = line.split(' ')
                        
                        for gar in substrs:
                                totalGarbage += int(gar)

                        finalLine += " " + str(totalGarbage)

                        finalHash[str(count*1000000)] = finalLine
                        
                        count = count + 1
      
        inputfile.close()
       
        inputfile = open(sys.argv[2], 'r')

        count = 1;

        for line in inputfile:

                if (line[0].isdigit()):
                        
                        finalLine = finalHash[str(count*1000000)]
                        totalGarbage = 0

                        substrs = line.split(' ')
                        
                        for gar in substrs:
                                totalGarbage += int(gar)

                        finalLine += " " + str(totalGarbage)
                        print str(count*1000000) + finalLine
                        count = count + 1

        inputfile.close()
