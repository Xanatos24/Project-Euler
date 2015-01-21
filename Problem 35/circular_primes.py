import numpy as np 

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    upper = int(np.ceil(n**0.5+1))

    for i in xrange(3,upper):
        if n % i == 0: return False
    return True


def rot_gen(n):
	number = str(n)
	start  = 0
	i 	   = 1
	while i<len(number):
		num = number[start+i]+number[start+i+1:]+number[:start+i]
		yield int(num)
		i=i+1


def prime_sieve(n):
	upper = n
	candidates = np.arange(upper+1)
	for i in np.arange(2,upper):
		if candidates[i]!=0:
			candidates[2*i::i] = 0
	c=[int(n) for n in candidates.tolist() if n not in [0,1]]
	return(c)

def rotations(n):
	number = str(n)
	start  = 0
	out	   = []
	for i in xrange(len(number)):
		o=number[start+i]+number[:start+i]+number[start+i+1:]
		out.append(int(o))
	return(out[1:])

primes = prime_sieve(1000000)

s = 0
for idx,prime in enumerate(primes):
	print round((idx/len(primes)),2)
	if '2' not in str(prime) and '5' not in str(prime):
		if all(y in primes for y in rot_gen(prime)): s=s+1
		
