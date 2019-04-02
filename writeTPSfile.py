#!/usr/bin/python
'''
usage: python writeTPSfile.py

Write TPS file for each specimen using folder name.

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor

May 22, 2010
'''

import glob
import re

path = '/Users/Lucy/Documents/2008-2010 Research/6_Morphometric Project/Morphometric Data/Mandible Shape/landmarks and sliding semilandmarks 2/2010 MCZ data'

foldername_re = re.compile(r'%s\/([0-9]*?)$' % (path))
imagename_re = re.compile(r'DSC_[0-9_]*?.JPG')

for folder in glob.iglob('%s/*' % (path)):
	foldersearch = foldername_re.findall(folder)
	foldername = foldersearch[0]
	list = []
	for file in glob.iglob('%s/%s/*.JPG' % (path,foldername)):
		imagesearch = imagename_re.findall(file)
		imagename = imagesearch[0]
		line = 'LM=0\nIMAGE=%s\nID=0' % (imagename)
		list.append(line)
	newtext = '\n'.join(list)
	outfilename = '%s/%s/%s.TPS' % (path,foldername,foldername)
	outfile = open(outfilename,'w')
	outfile.write(newtext)