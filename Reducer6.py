#!/usr/bin/python
import sys
Totalhits=0
oldkey=None
countpath=0
MostNumberOfPath=0
url=None
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,count=data
	if oldkey and newkey!=oldkey:
		if countpath>=MostNumberOfPath:
			MostNumberOfPath=countpath
			url=oldkey
		countpath=0
	oldkey=newkey
	countpath+=int(count)
if oldkey!=None:
	if countpath>=MostNumberOfPath:
			MostNumberOfPath=countpath
			url=oldkey
	print url,'\t',MostNumberOfPath
	
	
