#!/usr/bin/python

from pyx import *
import os, sys, re, string, operator, getopt, types

# Global Variables
labels = []

# Datafile should be the only argument
inDataFile = sys.argv[1]
outputfile = sys.argv[2]
cmdWidth = float(sys.argv[3])

# find the header line
infile = open(inDataFile,'r')
line = infile.readline()
commentline = ""

# Find the last comment line before an uncommented line
# This should have the column headers
while ((0 == len(commentline)) and (0 < len(line))):
	line = line.strip()
	line = line.rstrip()

	if (line[0] in ["#","!","%"]):
		commentline = line
	else:
		break

	line = infile.readline()
labels = commentline[1:].split(" ")[1:]
infile.close()

# xPos = 0
# yPos = 1
# zPos = 2
# yMin = None
# yMax = None
# xMin = None
# xMax = None
# infile.close()
# infile = open(inDataFile,'r')
# for line in infile:
# 	if (line[0].isdigit()):
# 		lineParts = line.split(" ")
# 		if(1 < len(lineParts)):
# 			if(None == xMin):
# 				xMin = int(lineParts[xPos])
# 			if(None == xMax):
# 				xMax = int(lineParts[xPos])
# 			if(None == yMin):
# 				yMin = int(lineParts[yPos])
# 			if(None == yMax):
# 				yMax = int(lineParts[yPos])
# 			if(int(lineParts[xPos]) > xMax):
# 				xMax = int(lineParts[xPos])
# 			if(int(lineParts[xPos]) < xMin):
# 				xMin = int(lineParts[xPos])
# 			if(int(lineParts[yPos]) > yMax):
# 				yMax = int(lineParts[yPos])
# 			if(int(lineParts[yPos]) < yMin):
# 				yMin = int(lineParts[yPos])
# infile.close()

#print "MIN:" + str(yMin) + "," + str(xMin) + " MAX:" + str(yMax) + "," + str(xMax)

# Do the line graph
	
g = graph.graphxy(width=cmdWidth,
  		  y=graph.axis.linear(title="SIN"),
		  x=graph.axis.linear(title="DIN"))

# Draw the graph
g.plot([graph.data.file(inDataFile, x=1, y=2)],
       [graph.style.symbol(graph.style.symbol.circle, size=0.005*unit.v_cm, symbolattrs=[deco.filled])])
g.writeEPSfile(outputfile)
