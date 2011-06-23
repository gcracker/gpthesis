#!/usr/bin/python

from pyx import *
import os, sys, re, string, operator, getopt, types

# Global Variables
labels = []

# Datafile should be the only argument
outputfile = sys.argv[1]
datafile = sys.argv[2]

# find the header line and max,min values
maxX = None
minX = None
maxY = None
minY = None
commentline = None

# Find the last comment line before an uncommented line
# This should have the column headers
infile = open(datafile,'r')
for line in infile:
	line = line.strip()
	
	if ((commentline == None) and 
	    (line[0] in ["#","!","%"])):
		commentline = line
	else:
		lineParts = line.split(" ")
		
		if((None == maxX) or
		   (int(lineParts[0]) > maxX)):
			maxX = int(lineParts[0])
		if((None == minX) or
		   (int(lineParts[0]) < minX)):
			minX = int(lineParts[0])
			
		# This should really be [1:
		for yVal in lineParts[1:]:
			if((None == maxY) or
			   (int(yVal) > maxY)):
				maxY = int(yVal)
			if((None == minY) or
			   (int(yVal) < minY)):
				minY = int(yVal)

if(-1 != commentline.find(",")):
	labels = commentline[1:].split(",")[1:]
else:
	labels = commentline[1:].split(" ")[1:]

infile.close()

# Do the line graph
maxY = int(maxY + (maxY / 4))

g = graph.graphxy(width=9, height=4.5,
		  key=graph.key.key(pos="br", hinside=1, dist=.1, vdist=1.3),
  		  y=graph.axis.linear(min=0, max=maxY , title="Removed Instructions"),
		  x=graph.axis.linear(min=minX, max=maxX, title="Slice Iteration"))

# Actually draw the graph
g.plot([graph.data.file(datafile, x=1, y=2, title=labels[0])],
       [graph.style.line([color.grey.black, style.linestyle.solid])])

if 1 < len(labels):
	g.plot([graph.data.file(datafile, x=1, y=3, title=labels[1])],
	       [graph.style.line([color.grey.black, style.linestyle.dashed])])

g.writeEPSfile(outputfile)
