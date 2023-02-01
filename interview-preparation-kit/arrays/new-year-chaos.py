#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes_count = 0
    q = [x - 1 for x in q]

    for (idx, v) in enumerate(q):
        if v - idx > 2:
            print('Too chaotic')
            return
        for x in range(max(v - 1, 0), idx):
            if q[x] > v:
                bribes_count += 1

    print(bribes_count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
