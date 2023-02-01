from itertools import combinations_with_replacement

if __name__ == '__main__':
    string, k = input().split()
    string = sorted(string)
    k = int(k)

    print('\n'.join(
        ''.join(x) for x in combinations_with_replacement(string, k)
    ))
