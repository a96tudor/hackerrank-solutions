import numpy

if __name__ == '__main__':
    a = numpy.array(list(map(float, input().split())))

    numpy.set_printoptions(legacy='1.13')

    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))
