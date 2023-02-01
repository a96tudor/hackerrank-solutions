import numpy

if __name__ == '__main__':
    a = numpy.array(list(map(int, input().split())))
    b = numpy.array(list(map(int, input().split())))

    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
