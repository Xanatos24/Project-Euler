import numpy as np
def countRoutes(n):
	result = 1
	for i in range(1,n+1):
		result = result * (n + i)/i
	return int(result)
# import scipy.misc as scm

# scm.comb(40,20,1)

