#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    countOfSwaps = 0
    for i in range(len(a)):
        countOfSwaps += len(list(x for x in a[i:] if x < a[i]))

    print(f'Array is sorted in {countOfSwaps} swaps.')
    print(f'First Element: {min(a)}')
    print(f'Last Element: {max(a)}')


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
