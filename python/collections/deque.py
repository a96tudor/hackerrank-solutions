from collections import deque

OPERATIONS = {
    'append': lambda d, x: d.append(x),
    'appendleft': lambda d, x: d.appendleft(x),
    'pop': lambda d, _: d.pop(),
    'popleft': lambda d, _: d.popleft()
}

if __name__ == '__main__':
    n = int(input())
    d = deque()

    for _ in range(n):
        data = input()
        if len(data.split()) == 1:
            command = data
            x = None
        else:
            command = data.split()[0]
            x = int(data.split()[1])

        OPERATIONS[command](d, x)

    print(' '.join(str(x) for x in d))
