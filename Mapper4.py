#!/usr/bin/python
import sys
for line in sys.stdin:
	data=line.strip().split(' ')
	if len(data)!=10:
		continue
	request,size=data[9],data[6]
	print size,'\t',size

	
