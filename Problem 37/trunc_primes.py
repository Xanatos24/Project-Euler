import numpy as np


def prime_sieve(n):
	upper = n
	candidates = np.arange(upper+1)
	for i in np.arange(2,upper):
		if candidates[i]!=0:
			candidates[2*i::i] = 0
	c=[int(n) for n in candidates.tolist() if n not in [0,1]]
	return(c)


def trunc_gen(n):
	number  = str(n)
	i 		= 1
	while i < len(number):
		yield int(number[i:])
		yield int(number[:len(number)-i])
		i = i+1

primes = prime_sieve(1000000)

out=[]
i = 4
while len(out)<11:
	prime = primes[i]
	if all(y in primes for y in trunc_gen(prime)): 
		print(prime)
		out.append(prime)
	i = i+1