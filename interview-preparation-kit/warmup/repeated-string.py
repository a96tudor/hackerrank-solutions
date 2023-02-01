#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    number_of_a_in_base_string = s.count('a')
    number_of_exact_repetitions = n // len(s)
    number_of_a_in_leftover = s[:(n % len(s))].count('a')

    return number_of_a_in_base_string * number_of_exact_repetitions + number_of_a_in_leftover


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
