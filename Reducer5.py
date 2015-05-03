#!/usr/bin/python
import sys
Totalhits=0
oldkey=None
countfromip=0
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,count=data
	if oldkey and newkey!=oldkey:
		print oldkey,'\t',countfromip
		countfromip=0
	oldkey=newkey
	countfromip+=int(count)
if oldkey!=None:
	print oldkey,'\t',countfromip
	
