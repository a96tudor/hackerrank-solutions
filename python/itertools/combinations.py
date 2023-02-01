from itertools import combinations

if __name__ == '__main__':
    string, k = input().split()
    string = sorted(string)
    k = int(k)

    for r in range(1, k + 1):
        print('\n'.join(''.join(x) for x in combinations(string, r)))
