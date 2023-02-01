import itertools

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(' '.join(str(x) for x in list(itertools.product(a, b))))
