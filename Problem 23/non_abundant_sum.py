import numpy as np 
def factors(n):
	out=[]
	upper = np.ceil(np.sqrt(n))+1
	for i in np.arange(1,upper):
		if n % i == 0:
			if n!=i:
				out.append(i)
	#print out
	out+=(n/np.array(out)).tolist()
	out=[int(o) for o in out if o!=n]
	if n!=1: out+=[1]
	return(sorted(list(set((out)))))

def sums(arr):
	out=set()
	for i in range(len(arr)):
		foo=(arr[i:]+arr[i])
		for f in foo:
			out.add(f)
	return(out)


d={}
a=[]
for i in xrange(1,28123+1):
	d[i]=sum(factors(i))
	if d[i]>i:
		a.append(i)
	print i

cands=sums(np.array(a))

cands=abundsums
total=0
for i in xrange(1,28133):
	if i not in cands:
		print(i)
		total+=i


