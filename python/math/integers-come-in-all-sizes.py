if __name__ == '__main__':
    a, b, c, d = tuple(map(int, [input() for _ in range(4)]))

    print(a ** b + c ** d)
