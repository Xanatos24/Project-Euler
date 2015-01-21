import numpy as np


def recip(n):
	cache=[]
	r = 1
	while r not in cache:
		cache.append(r)
		r = (r % n) * 10
	idx = cache.index(r)	
	return len(cache)-idx


out = []

for i in xrange(1,1001):
	print i
	out.append(recip(i))

out.index(max(out))+1