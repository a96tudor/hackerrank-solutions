#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps_count = 0
    arr = [x - 1 for x in arr]
    for idx in range(len(arr)):
        while arr[idx] != idx:
            val = arr[idx]
            swp = arr[val]
            arr[val] = val
            arr[idx] = swp

            swaps_count += 1

    return swaps_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
