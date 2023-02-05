def swap_case(s):
    return ''.join(c.swapcase() for c in s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
