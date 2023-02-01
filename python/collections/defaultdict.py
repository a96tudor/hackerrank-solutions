from collections import defaultdict

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    positions = defaultdict(list)

    for i in range(n):
        letter = input()
        positions[letter].append(i + 1)

    for _ in range(m):
        letter = input()
        if letter in positions:
            print(' '.join(str(x) for x in positions[letter]))
        else:
            print(-1)
