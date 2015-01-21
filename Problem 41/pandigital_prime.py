import numpy as np
from collections import Counter
def prime_sieve(n):
	upper = n
	candidates = np.arange(upper+1)
	for i in np.arange(2,upper):
		if candidates[i]!=0:
			candidates[2*i::i] = 0
	c=[int(n) for n in candidates.tolist() if n not in [0,1]]
	return(c)

def ispandigit(n):
	number = str(n)
	l 	   = len(number)
	x=set(range(1,l+1))==set([int(x) for x in str(number)])
	return(x)

primes = prime_sieve(987654321)

out=[]

for prime in primes:
	if ispandigit(prime): out.append(prime)