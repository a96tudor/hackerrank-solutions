#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    substrings = {}

    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            substring = ''.join(sorted(s[i:i + j]))
            if substring == '':
                continue
            if substring in substrings:
                substrings[substring] += 1
                continue
            substrings[substring] = 1

    return sum((x * (x - 1)) // 2 for x in substrings.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
