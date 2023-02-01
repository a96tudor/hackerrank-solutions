#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

ENGLISH_LETTERS = 'abcdefghijklmnoprqstuvwxyz'


def makeAnagram(a, b):
    letter_freq_a = Counter(a)
    letter_freq_b = Counter(b)

    count = sum(abs(letter_freq_a[l] - letter_freq_b[l]) for l in ENGLISH_LETTERS)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
