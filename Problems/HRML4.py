#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr=list(map(int,arr))
    arr.sort()
    s1=list(arr[0:4])
    s2=list(arr[1:5])
    s1=map(int,s1)
    s2=map(int,s2)
    a=sum(s1)
    b=sum(s2)
    print(a,b)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)