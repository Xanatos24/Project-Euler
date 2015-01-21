import numpy as np

def sieve(n):
	upper = n
	candidates = np.arange(upper+1)
	for i in np.arange(2,upper):
		if candidates[i]!=0:
			candidates[2*i::i] = 0
	c=[int(n) for n in candidates.tolist() if n not in [0,1]]
	return(c)


primes=sieve(2000000)
sum(primes)

