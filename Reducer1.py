#!/usr/bin/python
import sys
oldkey=None
totalcost=0
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,cost=data
	if oldkey and oldkey!=newkey:
		print oldkey,'\t',totalcost
		totalcost=0
	oldkey=newkey
	totalcost=totalcost + float(cost)
if oldkey!=None:
	print oldkey,'\t',totalcost

	

