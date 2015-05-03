#!/usr/bin/python
import sys
oldkey=None
HighestSale=0
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,Sale=data
	if float(Sale)>=HighestSale:
		HighestSale=float(Sale)
	if oldkey and newkey!=oldkey:
		print oldkey,'\t',HighestSale
		HighestSale=0
	oldkey=newkey
if oldkey!=None:
	print oldkey,'\t',HighestSale
