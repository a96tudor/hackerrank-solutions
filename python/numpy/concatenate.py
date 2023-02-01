import numpy

if __name__ == '__main__':
    n, m, _ = tuple(map(int, input().split()))

    a = numpy.array(
        [list(map(int, input().split())) for _ in range(n)]
    )
    b = numpy.array(
        [list(map(int, input().split())) for _ in range(m)]
    )

    print(numpy.concatenate((a, b), axis=0))

