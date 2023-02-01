OPERATIONS = {
    'pop': lambda s, x: s.pop(),
    'remove': lambda s, x: s.remove(x),
    'discard': lambda s, x: s.discard(x),
}


def perform_next_operation(s):
    a = input().split(' ')
    operation, x = a[0], a[-1]
    try:
        x = int(a[-1])
    except:
        pass

    OPERATIONS[operation](s, x)


if __name__ == '__main__':
    _ = int(input())
    s = set(map(int, input().split()))
    k = int(input())

    for _ in range(k):
        perform_next_operation(s)

    print(sum(s))

