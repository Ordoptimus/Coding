#codejam3 2020
import re

arr = []
c, stsol = 1, 0

t = int(input())
for i in range(0,t):
	arr.append(input())
print(arr)
for j in range(0,t):
	st = arr[j]
	ln = len(st)
	stsol = st
	for k in range(0,ln):
		if(stsol[k].isdigit()==True):
			n1 = int(stsol[k])
			while(c<=n1):
				stsol = "(" + stsol[k] + ")"
				c += 1
				ln += 2
	print(stsol)
		
