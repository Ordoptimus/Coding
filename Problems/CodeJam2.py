#codejam2 2020
#incomplete

arr, arrsol, arrint = [], [], []

def timecomp(arr,k,n):
	global arrint
	lockcount = 0
	while(k<n):
		if(arr[k][1]<=arr[k+1][0]):
				arrint.append("C")
		elif(k==n):
			break
		elif(lockcount>=n-1):
			arrint="IMPOSSIBLE"
			break
		else:
			lockcount += 1
			arrint.append("J")
			timecomp(arr,k+1,n)
t = int(input())
for i in range(0,t):
	n = int(input())
	for j in range(0,n):
		ar1 = [int(x) for x in input().split()]
		arr.append(ar1)
	timecomp(arr,0,n)
	print(arrint)
	arrsol.append(arrint)
		
		
		
	'''for k in range(0,n):
		if(arr[k][1]<=arr[k+1][0]):
			arrint.append("C")
		else:
			lockcount += 1'''
			
			
print(arrsol)