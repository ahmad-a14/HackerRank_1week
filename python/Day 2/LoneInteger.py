#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    sorted_arr = sorted(a)
    for i  in a:
        new_array = sorted_arr.copy()
        new_array.remove(i)
        if i not in new_array:
            return i
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()


#############################
def lonelyinteger(a):
    sorted_arr = sorted(a)
    for i in sorted_arr:
        if sorted_arr.count(i) == 1:
            return i
