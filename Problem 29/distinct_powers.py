import numpy as np

def powers(base,n):
	e = 2
	num = base ** e
	while e <= n:
		yield num
		e=e+1
		num = base ** e

out= set()

for i in range(2,101):
	print i
	out |= set(powers(i,100))
