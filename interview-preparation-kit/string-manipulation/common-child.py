#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def get_neighbours(lcs, i, j):
    return {
        'up': 0 if i == 0 else lcs[i - 1][j],
        'left': 0 if j == 0 else lcs[i][j - 1],
        'corner': 0 if i == 0 or j == 0 else lcs[i - 1][j - 1]
    }


def commonChild(s1, s2):
    lcs = [[0 for _ in range(len(s1))] for _ in range(len(s1))]

    for i in range(len(s1)):
        for j in range(len(s1)):
            neighbours = get_neighbours(lcs, i, j)

            if s1[i] == s2[j]:
                lcs[i][j] = neighbours['corner'] + 1
            else:
                lcs[i][j] = max(neighbours['up'], neighbours['left'])

    return lcs[len(s1) - 1][len(s2) - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
