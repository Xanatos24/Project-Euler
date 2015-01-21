import numpy as np


def palindrome(n):
	num = 1
	while num <= n:
		if str(num) == str(num)[::-1]:
			b = str(bin(num)[2:])
			if not b.startswith('0') and str(b) == str(b)[::-1]:
				yield num
		num = num + 1

sum(x for x in palindrome(1000000))

