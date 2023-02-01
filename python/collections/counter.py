from collections import Counter

if __name__ == '__main__':
    _ = input()

    stock = Counter(list(map(int, input().split())))
    total = 0

    t = int(input())

    for _ in range(t):
        size, price = tuple(map(int, input().split()))
        if stock[size] == 0:
            # We cannot sell to this person
            continue
        total += price
        stock[size] -= 1

    print(total)
