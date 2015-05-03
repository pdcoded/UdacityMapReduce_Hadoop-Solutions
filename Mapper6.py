#!/usr/bin/python
import sys
for line in sys.stdin:
	data=line.strip().split(' ')
	if len(data)!=10:
		continue
	if 'http://www.the-associates.co.uk' in data[6] and len(data[6])>len('http://www.the-associates.co.uk'):
		data[6]=data[6][data[6].index('k/')+1:]  #remove http://www.the-associates.co.uk from all paths
	if len(data[6])>1:
		print data[6],'\t',1  #remove path with only '/'

	
