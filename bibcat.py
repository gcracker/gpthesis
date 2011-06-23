#!/usr/bin/python
import sys
import os
import time
import datetime
import shutil
import subprocess

g_byPaperName = {}

if(1 < len(sys.argv):
      g_outfile = sys.argv[1]

for bibname in sys.argv[2:]:
