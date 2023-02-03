import re

if __name__ == '__main__':
    regex = r'([a-zA-Z0-9])\1'

    data = input()

    x = re.findall(regex, data)

    if x:
        print(x[0])
    else:
        print(-1)
