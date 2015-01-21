import numpy as np 

with open("p067_triangle.txt","r") as fh:
	txt=fh.read()
rows=[]
for line in txt.split("\n"):
	if line!="":
		rows.append([int(i) for i in line.split(" ")])

idx=len(rows)-2

def calcRow(rows, idx):
	for i in range(len(rows[idx])):
		print i
	    # add the largest of the values below-left or below-right
		rows[idx][i] += max([rows[idx+1][i],rows[idx+1][i+1]])
	if len(rows[idx])==1: 
		return rows[idx][0]
	else: 			
		return calcRow(rows, idx-1)

x=calcRow(rows, idx)