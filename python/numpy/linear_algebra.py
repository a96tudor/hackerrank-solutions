import numpy

if __name__ == '__main__':
    n = int(input())
    a = numpy.array(
        [list(map(float, input().split())) for _ in range(n)]
    )

    print(round(numpy.linalg.det(a), 2))
