if __name__ == '__main__':
    n = int(input())

    dist = set()

    for _ in range(n):
        stamp = input()
        dist.add(stamp)

    print(len(dist))
