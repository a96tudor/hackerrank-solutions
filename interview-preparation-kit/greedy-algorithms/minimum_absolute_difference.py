#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_dif = 10 ** 10

    for idx in range(len(arr) - 1):
        if abs(arr[idx] - arr[idx + 1]) < min_dif:
            min_dif = abs(arr[idx] - arr[idx + 1])

    return min_dif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
