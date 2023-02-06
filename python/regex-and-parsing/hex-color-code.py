import re

if __name__ == '__main__':
    n = int(input())

    regex = r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})'

    for _ in range(n):
        line = input()
        colors = re.findall(regex, line)
        if len(colors) > 0:
            print('\n'.join(colors))
