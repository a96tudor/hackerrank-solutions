if __name__ == '__main__':
    _ = input()
    english = set(map(int, input().split()))

    _ = input()
    french = set(map(int, input().split()))

    at_least_one = english.union(french)

    print(len(at_least_one))
