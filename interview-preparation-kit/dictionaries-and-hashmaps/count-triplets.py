#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):
    apps1 = Counter(arr)
    apps2 = Counter()

    result = 0

    for x in arr:
        y = x // r
        z = x * r

        apps1[x] -= 1

        if apps2[y] and apps1[z] and x % r == 0:
            result += apps2[y] * apps1[z]

        apps2[x] += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
