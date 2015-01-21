import numpy as np


def fifth(number,e=5):
	number = str(number)
	powers = [int(x)**e for x in number]
	arr    = np.array(powers)
	return(arr.sum())


out=[]

for i in xrange(2,1000000):
	print i
	s = fifth(i)
	if s==i: out.append(i)