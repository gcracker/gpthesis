#!/usr/bin/python
import sys
import re


if len(sys.argv) < 3:	
        print "I need more cowbell"
else:	
        outlist = ""
        inputfile = open(sys.argv[1], 'r')

        count = 0

        for line in inputfile:
                
                newline = ""

                if(line[0] != "#"):

                        for subLine in line.split(','):
                                
                                print subLine
                                
                                if ((subLine.find(".") == -1) and
                                    (subLine.find("#") == -1)):
                                        newline += str(int(subLine) / 60) + ","
                                else:
                                        newline += subLine + ",";
                        outlist += newline + "\n"
                else:
                        outlist += line + "\n"


        inputfile.close()
        outputfile = open(sys.argv[2],'w')

        print >> outputfile, outlist
        outputfile.close()
                                                
