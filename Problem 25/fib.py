import numpy as np 


# a generator that yields items instead of returning a list
def fib():
	a,b=0,1
	while True:
		yield a
		b = a + b
		yield b
		a = a + b

seq=fib()
a = seq.next()
c=0
while len(str(a))<1000:
	c+=1
	a = seq.next()
	#print a
print c