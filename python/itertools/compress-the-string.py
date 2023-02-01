import itertools

if __name__ == '__main__':
    string = input()
    to_print = []

    for x in itertools.groupby(string):
        to_print.append(f'({len(list(x[1]))}, {x[0]})')
    print(' '.join(to_print))
