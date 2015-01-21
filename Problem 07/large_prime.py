import numpy as np
def sieve(n):
	# upper = np.ceil(np.sqrt(n))
	upper = n
	candidates = np.arange(upper+1)
	for i in np.arange(2,upper):
		if candidates[i]!=0:
			candidates[2*i::i] = 0
	c=[int(n) for n in candidates.tolist() if n not in [0,1]]
	return(c)

total=0
s=1
while total<10001:
	total=len(sieve(s))
	s+=1000
	print total
out=sieve(s)
print out[10000]