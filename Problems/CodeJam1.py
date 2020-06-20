#codejam1 2020

arr, arrcol, arrrow, arrsol = [], [], [], []
trace, row, col, c = 0, 0, 0, 0

t = int(input())
for i in range(0,t):
	n = int(input())
	for j in range(0,n):		#building the matrix
		ar1 = [int(x) for x in input().split()]
		arr.append(ar1)
	for k in range(0,n):		#trace
		trace += arr[k][k]
	for l in range(0,n):		#rowcount
		for m in range(0,n):
			arrrow.append(arr[l][m])
		if len(arrrow) > len(set(arrrow)):
			row += 1
		arrrow = []
	for m in range(0,n):		#colcount
		for l in range(0,n):	#putting cols in lists
			arrcol.append(arr[l][m])
		if len(arrcol) > len(set(arrcol)):
			col += 1
		arrcol = []
	arrsol.append(trace)		#creating sol array
	arrsol.append(row)
	arrsol.append(col)
	trace, row, col = 0, 0, 0	#resetting variables
	ar1, arr = [], []

for o in range(0,t):			#printing sol
	print("Case #{}: {} {} {}".format(o+1,arrsol[o+c],arrsol[o+1+c],arrsol[o+2+c]))
	c += 2						#for jump of 3 in array