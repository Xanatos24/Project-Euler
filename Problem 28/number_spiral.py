import numpy as np


n=1001
layers=np.ceil(n/2)


curr = 1

out=[]
ms=range(2,2*int(layers)+1,2)
for m in ms:
	for i in xrange(4):
		curr = curr + m
		out.append(curr)
sum(out)+1