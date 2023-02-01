#!/bin/python

import sys


n = int(input())
arr = map(int, input().split(' '))

result = [
    str(arr[len(arr) - i - 1]) for i in range(len(arr))
]

print(" ".join(result))
