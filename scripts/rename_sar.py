#!/usr/bin/env python

import re

with open('./pdf_names.txt') as f:
    pdf_names = f.read().splitlines()

with open('./session_names_processed.txt') as f:
    session_names = f.read().splitlines()

for i in xrange(0,len(pdf_names)):
    print str(i+1).zfill(3) + '_-_' + pdf_names[i][:-4] + '_-_' + session_names[i] + pdf_names[i][-4:]

"""
for fileNameFull in os.listdir("."):
    fileName, fileExtension = os.path.splitext(fileNameFull)
    fileNameOrig = fileName
    #print fileName, fileExtension
    if fileName != fileNameOrig:
        newFilename=fileName + fileExtension
        os.rename(fileNameFull, newFilename)
        print "\n%s [RENAMED:] %s" % (fileNameFull, newFilename)

"""
