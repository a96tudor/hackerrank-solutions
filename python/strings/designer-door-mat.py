if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    # Building the top part
    base_pattern = '.|.'

    for i in range(1, n, 2):
        print((base_pattern * i).center(m, '-'))

    # Print the welcome in the middle
    print('WELCOME'.center(m, '-'))

    # Print the bottom part
    for i in range(n - 2, 0, -2):
        print((base_pattern * i).center(m, '-'))
