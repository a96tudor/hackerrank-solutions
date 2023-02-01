#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    freq = Counter(s)
    rev_chars = {c: freq[c] // 2 for c in freq}
    shuffle_chars = {c: freq[c] // 2 for c in freq}

    string = []

    for c in reversed(s):
        if rev_chars[c] > 0:
            while string and string[-1] > c and shuffle_chars[string[-1]] > 0:
                c_string = string.pop()
                rev_chars[c_string] += 1
                shuffle_chars[c_string] -= 1
            string.append(c)
            rev_chars[c] -= 1
        else:
            shuffle_chars[c] -= 1

    return ''.join(string)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
