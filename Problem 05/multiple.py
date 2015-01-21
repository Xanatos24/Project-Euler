import numpy as np 


dividers=np.array([11, 13, 14, 16, 17, 18, 19, 20])
x=np.ones(20)
n=0
while not np.all(x==0):
	n+=2520 # least common multiple of all these numbers
	x=n % dividers
	print n

