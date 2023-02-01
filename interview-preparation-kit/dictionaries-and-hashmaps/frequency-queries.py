#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    data = {}
    results = []
    for t, k in queries:
        if t == 1:
            # Append
            if k in data:
                data[k] += 1
            else:
                data[k] = 1
            continue
        if t == 2:
            # Delete
            if k in data and data[k] > 0:
                data[k] -= 1
            continue

        # Check
        if k in data.values():
            results.append(1)
        else:
            results.append(0)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
