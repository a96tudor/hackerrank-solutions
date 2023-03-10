#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq = Counter(s)
    c = Counter(freq.values())

    if len(c) <= 1:
        return 'YES'
    if len(c) > 2:
        return 'NO'
    print(c)

    if 1 in c.values() and (c[min(c.keys())] == 1 or (max(c.keys()) - min(c.keys()) == 1)):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
