#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    wordMap = {}
    for word in magazine:
        if word not in wordMap:
            wordMap[word] = 1
            continue
        wordMap[word] += 1

    for word in note:
        if wordMap.get(word, 0) == 0:
            print('No')
            return
        wordMap[word] -= 1

    print('Yes')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
