#!/usr/bin/python
'''
usage: python moveimagestofolders.py infile oldfolderpath

Create folder for each specimen, then move images corresponding to specimen to folder, using text file listing specimen number and corresponding image names.

e.g., python moveimagestofolders.py list2.txt /Users/Lucy/Documents/2008-2010\ Research/6_Morphometric\ Project/Images/MCZ/May\ 2010/Rotated

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor
Created May 17, 2010
Modified November 24, 2010
'''

import sys
import re
import shutil
import os

infile = sys.argv[1]
oldfolder = sys.argv[2]
file = open(infile, 'r')
list = file.readlines()
file.close()

foldername_re = re.compile(r'([0-9]*?)\t')
image_re = re.compile(r'(DSC_[0-9]*?.JPG)')

for item in list:
	foldername_search = foldername_re.findall(item)
	image_search = image_re.findall(item)
	foldername = foldername_search[0]
	os.mkdir('%s/%s' % (oldfolder,foldername))
	image1 = image_search[0]
	image2 = image_search[1]
	image3 = image_search[2]
	shutil.move('%s/%s' % (oldfolder,image1), '%s/%s' % (oldfolder,foldername))
	shutil.move('%s/%s' % (oldfolder,image2), '%s/%s' % (oldfolder,foldername))
	shutil.move('%s/%s' % (oldfolder,image3), '%s/%s' % (oldfolder,foldername))

print 'Files successfully moved!'