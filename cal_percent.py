#!/usr/bin/python
import sys


if len(sys.argv) < 3:   
    print "I need more cowbell"
else:   

    infiles = sys.argv[1:]
    fcol = []
    pcol1 = []
    pcol2 = []

    filenum = 0
    
    for file in infiles:

        inputfile = open(file, 'r')

        for line in inputfile:                
                 
            if(line[0] != "#"):
                linesplit = line.split(",")
                if(filenum == 0):
                    fcol.append(linesplit[0])
                    pcol1.append(linesplit[1])
                else:
                    pcol2.append(linesplit[1])

        filenum = filenum + 1
        
    print "#Trace,Percent"

    i = 0
    for strtemp in fcol:
        outstring =  strtemp + ","
        outstring = outstring + str(float(pcol1[i])/float(pcol2[i]))
        print outstring
        i = i + 1
        