import numpy as np 


with open("p042_words.txt","r") as fh:
	txt=fh.read().replace('"',"").split(",")


def a_value(s):
	CHARS={ chr(n):(n-64) for n in range(65,91)}
	CHARS['"']=0
	return sum(CHARS[a] for a in s)

def triangle(number):
	n 	= 1
	num = 0
	while num <= number:
		num = int(0.5*n*(n+1))
		yield num
		n 	= n + 1


vs=[a_value(x) for x in txt]



triangles = list(triangle(max(vs)))

l = [x for x in vs if x in triangles]