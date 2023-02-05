#!/bin/python3

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(tuple(map(int, input().rstrip().split())))
    k = int(input())

    arr = sorted(arr, key=lambda x: x[k])

    print(
        '\n'.join(' '.join(map(str, x)) for x in arr)
    )
