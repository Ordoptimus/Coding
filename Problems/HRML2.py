#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    #for i in range(0,ar_count-1):
        #ar[i] = ar[i+1]  (learning)
    #return ar[ar_count-1]
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()