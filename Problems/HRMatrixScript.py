#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix, baselst, fbaselst, tfinallst, finallst, fappnd, lappnd = [], [], [], [], [], [], []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in matrix:
    baselst.append(list(i))
for j in baselst:
    for k in j:
        fbaselst.append(k)
#print(fbaselst)
for l in range(0,m):
    tfinallst.append(fbaselst[l::3])
#print(tfinallst)
for o in tfinallst:
    for p in o:
        finallst.append(p)
basestr = ''.join(map(str,finallst))
#print(basestr)
for q in basestr:
    if(q.isalpha()==True or q.isdigit()==True):
        break
    else:
        fappnd.append(q)
        basestr.replace(q,'')
r = len(basestr)-1
while r>=0:
    if(basestr[r].isalpha()==True or basestr[r].isdigit()==True):
        break
    else:
        lappnd.append(basestr[r])
        basestr.replace(basestr[r],'')
    r -= 1
lappnd.reverse()
#lappnd = ' '.join(map(str,lappnd))
#fappnd = ' '.join(map(str,fappnd))
#print(basestr)
#print(fappnd)
#print(lappnd)
final = re.sub('[^a-zA-Z0-9 \n\.]', ' ', basestr)
final = final.replace('  ',' ')
final = list(final)
#print(final)
u = len(final)-1
while u>0:
    if(final[u]==' '):
        final[u] = ''
    else:
        break
    u -= 1
for v in final:
    if(v==' '):
        v = ''
    else:
        break
#print(final)
final = fappnd + final + lappnd
final = ''.join(map(str,final))
print(final)
