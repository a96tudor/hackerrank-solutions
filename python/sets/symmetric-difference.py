if __name__ == '__main__':
    _ = input()
    a = set(int(x) for x in input().split(' '))

    _ = input()
    b = set(int(x) for x in input().split(' '))

    sd = a.symmetric_difference(b)
    print('\n'.join(str(x) for x in sorted(sd)))
