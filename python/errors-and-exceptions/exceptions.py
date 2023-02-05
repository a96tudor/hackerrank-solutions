if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        try:
            a, b = tuple(map(int, input().split()))
        except ValueError as err:
            print(f'Error Code: {err}')
            continue

        try:
            print(int(a / b))
        except ZeroDivisionError:
            print('Error Code: integer division or modulo by zero')
