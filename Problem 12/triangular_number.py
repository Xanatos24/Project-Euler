import numpy as np

def lenFactors(n):
	cs= np.arange(np.sqrt(n))
	return(sum(n % cs == 0))

c=1
l2=0
while l2<500:
	n=sum(np.arange(1,c+1))
	l=lenFactors(n)
	l2=get_factors(int(n))
	print "Number: %d    Factors: %d" %(n,l2)
	c+=1


test=[sum(range(c+1)) for c in range(1,100000000)]



def get_factors(n):
    return sum(2 for i in range(1, int(math.sqrt(n)+1)) if not n % i)

test=[76576499,76576500]

for i in test:
	l2=lenFactors(int(i))
	print "Number: %d    Factors: %d" %(i,l2)
	if l2 > 500:
		break


#49995000