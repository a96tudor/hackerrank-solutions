if __name__ == '__main__':
    _ = input()
    english = set(map(int, input().split()))

    _ = input()
    french = set(map(int, input().split()))

    print(len(english.intersection(french)))

