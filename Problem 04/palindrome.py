import numpy as np

def sieve(n):
	digits=np.arange(n,1,-1)
	out=[]
	for x in range(len(digits)):
		candidates=digits[x] * digits[x:]
		for c in candidates:
			if str(c) == str(c)[::-1]:
				out.append(c)
	return out

max(sieve(999))