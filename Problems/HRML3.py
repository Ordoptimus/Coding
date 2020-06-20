#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    arr1=[]
    for x in arr:
        for y in x:
            arr1.append(y)
    a=n+1
    b=n-1
    s1=list(arr1[::a])
    s2=list(arr1[b:-b:b])
    s1=map(int,s1)
    s2=map(int,s2)
    sum1=sum(s1)
    sum2=sum(s2)
    res=sum1-sum2
    return abs(res)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()