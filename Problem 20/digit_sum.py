import numpy as np 
from scipy.misc import factorial

i=factorial(100,True)
arr=np.array(list(str(i)), dtype=int)
arr.sum()