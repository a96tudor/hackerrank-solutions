import numpy

if __name__ == '__main__':
    coeff = list(map(float, input().split()))
    x = float(input())

    print(numpy.polyval(coeff, x))
