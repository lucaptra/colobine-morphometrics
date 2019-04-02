#!/bin/usr/python
'''
usage: python convert_tpssmall_output.py infile outfile

e.g., python convert_tpssmall_output.py tpssmall_39spp_report.txt MCZ2010_39spp_erroranalysis.xls

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor
June 7, 2010
'''

import sys
import re

infile = sys.argv[1]
outfilename = sys.argv[2]
file = open(infile,'r')
text = file.read()
file.close()

specimen_re = re.compile(r'H:\\analyze\\error analysis\\(.*?).TPS\r')
min_re = re.compile(r'tatistics for distance to reference:\r\n Statistic  Procrustes d     Tangent d\r\n       Min      (.*?)      0')
max_re = re.compile(r'Statistics for distance to reference:\r\n Statistic  Procrustes d     Tangent d\r\n       Min      .*?      .*?\r\n       Max      (.*?)      0')
mean_re = re.compile(r'Statistics for distance to reference:\r\n Statistic  Procrustes d     Tangent d\r\n       Min      .*?      .*?\r\n       Max      .*?      .*?\r\n      Mean      (.*?)      0')

specimen = specimen_re.findall(text)
min = min_re.findall(text)
max = max_re.findall(text)
mean = mean_re.findall(text)

list = ['specimen\tmin\tmax\tmean\n']
for x in range(len(specimen)):
	line = specimen[x] + '\t' + str(min[x]) + '\t' + str(max[x]) + '\t' + str(mean[x]) + '\n'
	list.append(line)

newlist = ''.join(list)
outfile = open(outfilename,'w')
outfile.write(newlist)