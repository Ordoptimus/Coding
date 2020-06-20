a = []
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
#a = list(map(int, a))  (also learning)
#b = list(map(int, b))
a.sort()
b.sort()
res=list(product(a, b))
res = [str(a) for a in res]
print(' '.join(res))