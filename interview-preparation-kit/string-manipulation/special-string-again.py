#!/bin/python3

import math
import os
import random
import re
import sys


def build_freq_list(s):
    freq_s = []
    current = s[0]
    current_count = 1

    for letter in s[1:]:
        if letter == current:
            current_count += 1
            continue
        freq_s.append((current, current_count))
        current_count = 1
        current = letter

    freq_s.append((current, current_count))

    return freq_s


# Complete the substrCount function below.
def substrCount(n, s):
    freq_s = build_freq_list(s)
    total = sum([(f[1] * (f[1] + 1)) // 2 for f in freq_s])

    for idx in range(1, len(freq_s) - 1):
        if freq_s[idx - 1][0] == freq_s[idx + 1][0] and freq_s[idx][1] == 1:
            total += min(freq_s[idx - 1][1], freq_s[idx + 1][1])

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
