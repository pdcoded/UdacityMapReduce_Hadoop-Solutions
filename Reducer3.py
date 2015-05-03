#!/usr/bin/python
import sys
oldkey=None
totalNumberOfSales=0
TotalSales=0
SalesPerStore=0
NumberOfSalesPerStore=0
for line in sys.stdin:
	data=line.strip().split('\t')
	if len(data)!=2:
		continue
	newkey,Sales=data
	if oldkey and newkey!=oldkey:
		TotalSales+=float(SalesPerStore)
		SalesPerStore=0
		totalNumberOfSales+=NumberOfSalesPerStore
		NumberOfSalesPerStore=0
	oldkey=newkey
	SalesPerStore+=float(Sales)
	NumberOfSalesPerStore+=1
if oldkey!=None:
	print TotalSales+SalesPerStore,'\t',totalNumberOfSales+NumberOfSalesPerStore

