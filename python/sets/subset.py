def solve_test_case():
    _ = input()
    a = set(map(int, input().split()))

    _ = input()
    b = set(map(int, input().split()))

    print(a == a.intersection(b))


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        solve_test_case()
