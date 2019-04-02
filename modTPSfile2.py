#!/usr/bin/python
'''
usage: python modTPSfile2.py

Concatenate digitized landmark data from TPS files into new file.

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor
May 28, 2010
'''

import glob
import re

folderpath = '/Volumes/Lucy/digitize 2'

TPSlist = []
numlist = []
for folder in glob.iglob('%s/*' % (folderpath)):
	for file in glob.iglob('%s/*_2.TPS' % (folder)):
		infile = open(file,'r')
		text = infile.read()
		TPSlist.append(text)
		filename_re = re.compile(r'%s/(.*?)_2.TPS' % (folder))
		filename = filename_re.findall(file)
		filename2 = filename[0]
		numlist.append(filename2)
TPSfile = '\n'.join(TPSlist)
specfile = '\n'.join(numlist)	#list of specimen names in TPSfile
outfile1 = open('%s/MCZ2010data.TPS' % (folderpath),'w')
outfile1.write(TPSfile)
outfile1 = open('%s/MCZ2010data_specimenlist.txt' % (folderpath),'w')
outfile1.write(specfile)