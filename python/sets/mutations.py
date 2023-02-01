# Enter your code here. Read input from STDIN. Print output to STDOUT

OPERATIONS = {
    'update': lambda a, s: a.update(s),
    'intersection_update': lambda a, s: a.intersection_update(s),
    'difference_update': lambda a, s: a.difference_update(s),
    'symmetric_difference_update': lambda a, s: a.symmetric_difference_update(s),
}


def process_next_line(a):
    x = input().split(' ')
    operation, l = x[0], int(x[1])
    s = set(int(x) for x in input().split(' '))

    a = OPERATIONS[operation](a, s)


if __name__ == '__main__':
    _ = input()
    a = set(int(x) for x in input().split(' '))

    t = int(input())

    for _ in range(t):
        process_next_line(a)

    print(sum(a))
