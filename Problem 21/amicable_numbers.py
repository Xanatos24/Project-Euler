import numpy as np 

def factors(n):
	out=[]
	upper = np.ceil(np.sqrt(n))
	#candidates = np.arange(upper+1)
	for i in np.arange(1,upper):
		if n % i == 0:
			out.append(i)
	out+=(n/np.array(out)).tolist()
	out+=[1]
	return(sorted(out))

d={}
for i in xrange(1,10000):
	a = int(sum(factors(i)))
	d[i] = a 

out=[]
for number in d:
	f = d[number]
	if f in d and f!=number:
		if d[f] == number :
			out.append((f, number))

res=np.array(out).sum()/2
print(res)