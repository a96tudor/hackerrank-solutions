import itertools

if __name__ == '__main__':
    _ = input()
    string = ''.join(input().split())
    k = int(input())
    count_all = 0
    count_a = 0

    for combination in itertools.combinations(string, k):
        if 'a' in combination:
            count_a += 1
        count_all += 1

    print(round(count_a / count_all, 5))
