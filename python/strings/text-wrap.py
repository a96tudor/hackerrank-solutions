

def wrap(string, max_width):
    return '\n'.join(string[idx:idx+max_width] for idx in range(0, len(string), max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
