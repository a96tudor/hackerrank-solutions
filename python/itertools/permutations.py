from itertools import permutations

if __name__ == '__main__':
    string, k = input().split()
    k = int(k)
    string = sorted(string)

    print('\n'.join(''.join(x) for x in permutations(string, k)))
