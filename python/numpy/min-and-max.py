import numpy

if __name__ == '__main__':
    n, _ = tuple(map(int, input().split()))

    a = numpy.array(
        [list(map(int, input().split())) for _ in range(n)]
    )

    print(numpy.max(numpy.min(a, 1)))
