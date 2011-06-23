#!/usr/bin/python
import shutil
import sys
import re


if len(sys.argv) < 3:	
        print "I need more cowbell"
        print "[Pattern] [Replacement] [String]"
else:		
        newFile = re.sub(sys.argv[1], sys.argv[2], sys.argv[3])

        if (newFile != sys.argv[3]):
                print newFile                    
                shutil.copy2(sys.argv[3], newFile)
     
#"\.e\d{3}" "_withGC.raw" "zddtest_176gccRunRef1_dinvssin_073009.e189"
