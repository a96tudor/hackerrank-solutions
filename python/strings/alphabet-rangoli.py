def print_rangoli(size):
    start_chr = ord('a')
    end_chr = ord('a') + size - 1

    line_length = 4 * size - 3

    # top part
    for line in range(1, size):
        chrs_left = [chr(c) for c in range(end_chr, end_chr - line, -1)]
        chrs_right = [chr(c) for c in range(end_chr - line + 2, end_chr + 1)]
        chrs = chrs_left + chrs_right
        print('-'.join(chrs).center(line_length, '-'))

    # center line
    chrs_left = [chr(c) for c in range(end_chr, end_chr - size, -1)]
    chrs_right = [chr(c) for c in range(end_chr - size + 2, end_chr + 1)]
    chrs = chrs_left + chrs_right
    print('-'.join(chrs).center(line_length, '-'))

    # borrom part
    # top part
    for line in range(size - 1, 0, -1):
        chrs_left = [chr(c) for c in range(end_chr, end_chr - line, -1)]
        chrs_right = [chr(c) for c in range(end_chr - line + 2, end_chr + 1)]
        chrs = chrs_left + chrs_right
        print('-'.join(chrs).center(line_length, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
