import re

if __name__ == '__main__':
    s = input()
    k = input()

    current_start = 0
    found_match = False
    while current_start < len(s):
        match = re.search(k, s[current_start:])
        if match is not None:
            found_match = True
            print((current_start + match.start(), current_start + match.end() - 1))
            current_start += match.start() + 1
        else:
            current_start = len(s)

    if not found_match:
        print((-1, -1))
