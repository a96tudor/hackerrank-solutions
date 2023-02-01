import numpy

if __name__ == '__main__':
    a = numpy.array(list(map(int, input().split())))
    print(numpy.reshape(a, (3, 3)))
