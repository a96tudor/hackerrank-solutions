import cmath

if __name__ == '__main__':
    z = complex(input())
    print('\n'.join(str(x) for x in cmath.polar(z)))
