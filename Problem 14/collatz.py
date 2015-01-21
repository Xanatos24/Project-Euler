import numpy as np 
import time

# a generator that yields items instead of returning a list
def collatz(n):
	num = n
	yield num
	while num > 1:
		#print num
		if num%2==0:
			num = num/2
		else:
	   		num = (3*num+1)
	   	yield num

t0 = time.time()
out=[]
cache={}
for i in xrange(1,10001):
	#print i
	out.append(sum(1 for _ in collatz(i)))
t1 = time.time()
print t1-t0
# np.argmax(out)+1

t0 = time.time()
out=[]
cache={}
for i in xrange(1,10001):
	#print i
	out.append(len(list(collatz(i))))
t1 = time.time()
print t1-t0