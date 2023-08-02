#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    
    arraySize = len(arr)
    for i in arr:
        if i < 0:
            negative = negative + 1
        elif i > 0 :
            positive = positive + 1
        else: 
            zeros = zeros + 1
    
            
    print(f"{positive/arraySize:.6f}")
    print(f"{negative/arraySize:.6f}")
    print(f"{zeros/arraySize:.6f}")
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
