#!/usr/bin/python
'''
usage: python rotateImage.py extension degree

Rotate an image using the PIL image library.
Modified from code available at http://www.daniweb.com/code/snippet216426.html.

Lucy Tran
Department of Ecology and Evolutionary Biology
University of Michigan, Ann Arbor
May 12, 2010
'''

import sys
import glob
import re
from PIL import Image

extension = sys.argv[1]
deg = sys.argv[2]	#specify degrees to rotate image
deg2 = float(deg)

for x in glob.iglob('*.%s' % (extension)):
	image1 = Image.open(x)		#open image file
	image2 = image1.rotate(deg2)	#rotate image
	#brings up modified image in viewer, saves as bitmap to temporary file, and calls viewer associated with .bmp
	#image2.show()
	file_re = re.compile(r'([A-Z0-9_]*?).JPG')
	file = file_re.findall(x)
	file2 = file[0]
	filename = '%s_2.%s' % (file2,extension)
	image2.save(filename)