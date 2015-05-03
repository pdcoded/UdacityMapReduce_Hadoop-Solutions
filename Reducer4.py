#!/usr/bin/python
import sys
Totalcount=0
oldkey=None
count=0
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,url=data
	if oldkey and newkey!=oldkey:
		Totalcount+=count
		count=0
	oldkey=newkey
	if url=='/assets/js/the-associates.js':
		count+=1
if oldkey!=None:
	print Totalcount+count
	
