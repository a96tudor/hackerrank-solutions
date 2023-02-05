CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def remove_duplicates(string):
    used_characters = {c: False for c in CHARACTERS}
    result = []

    for c in string:
        if not used_characters[c]:
            result.append(c)
            used_characters[c] = True

    return ''.join(result)


def merge_the_tools(string, k):
    strings = [remove_duplicates(string[i:i + k]) for i in range(0, len(string), k)]
    print('\n'.join(strings))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
