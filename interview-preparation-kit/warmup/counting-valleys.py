#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    in_valley = False
    level = 0
    valleys = 0

    for direction in path:
        if direction == 'D':
            level -= 1
        if direction == 'U':
            level += 1

        if level < 0 and not in_valley:
            in_valley = True

        if level == 0 and in_valley:
            in_valley = False
            valleys += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
