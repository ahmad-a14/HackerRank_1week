#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    minSum = 0
    maxSum = 0
    for i in range(0,len(arr)-1):
        val = sorted_arr[i]
        minSum = minSum + val
        
    for i in range(1,len(arr)):
        val = sorted_arr[i]
        maxSum = maxSum + val
        
    print (F"{minSum} {maxSum}")    
            
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)



############################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    minSum = sum(sorted_arr[:4])
    maxSum = sum(sorted_arr[-4:])
    
    print(minSum, maxSum)
    
            
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
