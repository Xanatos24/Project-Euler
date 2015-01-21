import numpy as np

def triplet():
	for n in xrange(1,200):
		for m in xrange(n+1,200):
			a = (m**2)-(n**2)
			b = 2 * m *n 
			c = (m**2) + (n ** 2)
			s = a+b+c
			if s==1000:
				return(a,b,c)
	return False

a,b,c=triplet()
print "Product = %d" % (a*b*c)
print "a = %d, b = %d, c = %d" % (a, b, c)
