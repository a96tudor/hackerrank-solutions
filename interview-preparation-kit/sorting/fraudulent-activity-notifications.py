#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def get_treshold(freq, n):
    keys = sorted(dict(freq).keys())
    count = 0
    arr = []

    m1 = n // 2
    m2 = n // 2 + 1

    for key in keys:
        count += freq[key]

        if len(arr) == 0 and m1 <= count:
            arr.append(key)
        if m2 <= count:
            arr.append(key)
            break

    if n % 2 == 1:
        return arr[-1] * 2

    return sum(arr)


def activityNotifications(expenditure, d):
    freq = Counter(expenditure[:d])
    idx = 0
    count = 0

    for exp in expenditure[d:]:
        treshold = get_treshold(freq, d)
        if exp >= treshold:
            count += 1
        freq[exp] += 1
        freq[expenditure[idx]] -= 1
        idx += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
