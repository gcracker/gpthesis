#!/usr/bin/python
import sys
import re


if len(sys.argv) < 3:	
        print "I need more cowbell"
else:	
        outlist = ""
        inputfile = open(sys.argv[1], 'r')

#        subStr = re.compile(',')

        count = 0

        for line in inputfile:

                m = re.match('.+\sPass\s', line)

                if m:
                        outlist = outlist + line

                m = re.match('Loading File:', line)

                if m:
                        outlist = outlist + line
                 
                m = re.match('Time for search is\s(\d+.\d+)', line)

                if m:
                        outlist = outlist + line
#                 if (line[0].isdigit()):
#                         line = subStr.sub(' ', line)                            
#                         outlist = outlist + line

#                else:
#                        outlist = outlist + "\n"
                

        inputfile.close()
        outputfile = open(sys.argv[2],'w')

        print >> outputfile, outlist
        outputfile.close()
                                                
