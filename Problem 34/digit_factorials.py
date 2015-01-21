import numpy as np
from scipy.misc import factorial

def fac(number):
	number = str(number)
	powers = [factorial(int(x), exact=True) for x in number]
	arr    = np.array(powers)
	return(arr.sum())


out=[]

for i in xrange(3,1000000):
	print i
	s = fac(i)
	if s==i: out.append(i)