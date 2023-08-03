#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # # Write your code here
    # pairs = 0
    
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i] - arr[j] == k:
    #             pairs += 1 
    # return pairs

    element_freq = {}
    for num in arr:
        element_freq[num] = element_freq.get(num, 0) + 1

    pairs_count = 0

    for num in arr:
    # Check if (num - k) exists in the dictionary and add its frequency to the pairs count
        pairs_count += element_freq.get(num - k, 0)

    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
