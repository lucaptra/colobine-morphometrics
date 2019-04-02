#!/usr/bin/python
'''
usage: python modTPSfile.py

Capture digitized landmark data for first image in each TPS file.

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor
May 28, 2010
'''

import glob
import re

folderpath = '/Users/Lucy/Desktop/digitize'

for folder in glob.iglob('%s/*' % (folderpath)):
	for file in glob.iglob('%s/*.TPS' % (folder)):
		infile = open(file,'r')
		text = infile.read()
		filename_re = re.compile(r'%s/(.*?).TPS' % (folder))
		filename = filename_re.findall(file)
		filename2 = filename[0]
		lsl_re = re.compile(r'(^LM=10(?:\s|.)*?ID=0)')
		lsl = lsl_re.findall(text)
		lsltext = lsl[0]
		outfile = open('%s/%s_2.TPS' % (folder,filename2),'w')
		outfile.write(lsltext)