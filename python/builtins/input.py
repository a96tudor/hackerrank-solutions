if __name__ == '__main__':
    x, y = tuple(map(int, input().split()))

    poly_string = input()
    poly_string = poly_string.replace('x', str(x))

    print(eval(poly_string) == y)
