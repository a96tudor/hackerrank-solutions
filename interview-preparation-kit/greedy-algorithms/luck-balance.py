#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    unimportant_contests = [x[0] for x in contests if x[1] == 0]
    important_contests = sorted([x[0] for x in contests if x[1] == 1], reverse=True)

    return sum(unimportant_contests) + sum(important_contests[:k]) - sum(important_contests[k:])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
