import numpy

if __name__ == '__main__':
    shape = tuple(map(int, input().split()))

    print(numpy.zeros(shape, int))
    print(numpy.ones(shape, int))
