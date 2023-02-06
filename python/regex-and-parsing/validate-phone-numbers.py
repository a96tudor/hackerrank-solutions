import re

if __name__ == '__main__':
    regex = r'^[789][0-9]{9}$'

    n = int(input())
    for _ in range(n):
        line = input()

        if re.match(regex, line):
            print('YES')
        else:
            print('NO')
