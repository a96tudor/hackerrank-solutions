def get_binary(x, padding):
    return f'{x:b}'.rjust(padding)


def get_octal(x, padding):
    return f'{x:o}'.rjust(padding)


def get_hexa(x, padding):
    return hex(x)[2:].rjust(padding).upper()


def print_formatted(number):
    padding = len(get_binary(number, 0))

    for x in range(1, number + 1):
        value = str(x).rjust(padding)
        binary = get_binary(x, padding)
        octal = get_octal(x, padding)
        hexa = get_hexa(x, padding)
        print(f'{value} {octal} {hexa} {binary}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)