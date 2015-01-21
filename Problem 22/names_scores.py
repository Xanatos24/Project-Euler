

with open("p022_names.txt") as fh:
	txt=fh.read().replace('\"','').split(",")


txt.sort()

def a_value(s):
	CHARS={ chr(n):(n-64) for n in range(65,91)}
	CHARS['"']=0
	return sum(CHARS[a] for a in s)

total=0
for idx,name in enumerate(txt):
	s = a_value(name)
	t = (idx+1) * s
	print idx,s,t
	total += t
