def is_strict_superset(a, x):
    return x == a.intersection(x) and a != a.intersection(x)


if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())
    cnt = 0

    for _ in range(n):
        x = set(map(int, input().split()))
        if not is_strict_superset(a, x):
            print('False')
            break
        cnt += 1

    if cnt == n:
        print('True')
