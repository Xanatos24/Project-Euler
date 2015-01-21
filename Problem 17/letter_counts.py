from num2words import num2words
import re

out=0
for i in xrange(1,1001):
	x=num2words(i)
	x=re.sub(r"[ -]","",x)
	out+=len(x)