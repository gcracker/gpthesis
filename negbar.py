#!/usr/bin/python

from pyx import *
import os, sys, re, string, operator, getopt, types


# Global Variables
labels = []

# Datafile should be the only argument
outputfile = sys.argv[1]
datafile = sys.argv[2]

infile = open(datafile,'r')
for line in infile:
	line = line.strip()
	
	if ((commentline == None) and 
	    (line[0] in ["#","!","%"])):
		commentline = line

if(-1 != commentline.find(",")):
	labels = commentline[1:].split(",")[1:]
else:
	labels = commentline[1:].split(" ")[1:]

infile.close()

a = graph.axis.bar(multisubaxis=graph.axis.bar(dist=0))

g = graph.graphxy(width=8, x=a)
g.plot([graph.data.list([["A", 5], ["B", 6]], xname=1, y=2),
        graph.data.list([["A", -7], ["B", 8], ["C", 9]], xname=1, y=2)],
       [graph.style.barpos(fromvalue=0), graph.style.bar()])
g.writeEPSfile("multisubaxis")
