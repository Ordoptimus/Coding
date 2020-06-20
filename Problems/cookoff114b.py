# cook your dish here
tst=int(input())
for i in range(0,tst):
    arm=[]
    n=int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    l=len(arr)
    for j in range(0,3*arr[-1]):
        if(j in arr):
            arm.append(j)
        else:
            for k in range(0,l):
                if(j%arr[k]==0):
                    arm.append(j)
                else:
                    continue
    arm = list(set(arm)) 
    print(arm)
    l1=len(arm)
    dis=0
    for m in range(0,l1-1):
        distemp=arm[m+1]-arm[m]
        if(distemp>dis):
            dis=distemp
    print(dis)
