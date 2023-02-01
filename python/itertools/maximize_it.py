import itertools

if __name__ == '__main__':
    k, m = tuple(map(int, input().split()))

    lists = []
    max_sum = 0

    for _ in range(k):
        lists.append(list(map(int, input().split()[1:])))

    for combination in itertools.product(*lists):
        result = sum(x ** 2 for x in combination) % m
        if result > max_sum:
            max_sum = result

    print(max_sum)
