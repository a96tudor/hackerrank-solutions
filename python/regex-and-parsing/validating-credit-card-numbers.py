import re

if __name__ == '__main__':
    format_regex = r'^[4-6][0-9]{3}(\-?[0-9]{4}){3}$'
    repeated_regex = r'([\d])\1\1\1'

    n = int(input())

    for _ in range(n):
        string = input()

        if re.match(format_regex, string):
            if not re.search(repeated_regex, string.replace('-', '')):
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')
