#!/usr/bin/python
import sys
import re


if len(sys.argv) < 3:	
        print "I need more cowbell"
else:	
        outlist = ""
        inputfile = open(sys.argv[1], 'r')

        subStr = re.compile(',')

        count = 0
        finalLine = ""

        for line in inputfile:
                
                if (line[0].isdigit()):
                        line = subStr.sub(' ', line)
                        outlist = outlist + line
                        
                        #                m = re.match('Time for garbage collection:\s(\d+)', line)
#                m = re.match('Number of BDD and ADD nodes:\s(\d+)', line)
#                m = re.match('Number of ZDD nodes:\s(\d+)', line)
                m = re.match('Opcount:',line)

                if m:
#                        gctime = m.group(1)
                        cleanIn = re.match('.+test_(.+)RunRef.+(dinvs(din|sin|rdy))', sys.argv[1])
                        type = cleanIn.group(1) + "." + cleanIn.group(2)
#                        print type + ": " + gctime
                        finalLine = type + ": " + line

                
                else:
                        outlist = outlist + "\n"
                

        print finalLine

        inputfile.close()
	outputfile = open(sys.argv[2],'w')
	
	print >> outputfile, outlist
	outputfile.close()
                                                
