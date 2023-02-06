import re

if __name__ == '__main__':
    n = int(input())
    regex_and = r' && '
    regex_or = r' \|\| '

    for _ in range(n):
        line = input()
        while re.search(regex_and, line):
            line = re.sub(regex_and, ' and ', line)
        while re.search(regex_or, line):
            line = re.sub(regex_or, ' or ', line)
        print(line)
