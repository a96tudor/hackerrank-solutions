import numpy

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    numpy.set_printoptions(legacy='1.13')
    print(numpy.eye(n, m))
