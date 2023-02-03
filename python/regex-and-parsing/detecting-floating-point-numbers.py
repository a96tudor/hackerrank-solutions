import re

if __name__ == '__main__':
    n = int(input())

    regex = r'^[+-]?[0-9]*\.[0-9]+$'

    for _ in range(n):
        string = input()
        if re.search(regex, string):
            print(True)
        else:
            print(False)
