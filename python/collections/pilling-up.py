from collections import deque


def get_max_value(d):
    if len(d) == 1:
        return d.pop()

    left = d.popleft()
    right = d.pop()

    if left > right:
        d.append(right)
        return left
    else:
        d.appendleft(left)
        return right


def check_if_possible(arr):
    d = deque(arr)
    last_size = 2 ** 32

    while len(d) > 0:
        to_add = get_max_value(d)
        if to_add > last_size:
            return False
        last_size = to_add

    return True


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        _ = input()
        array = list(map(int, input().split()))

        if check_if_possible(array):
            print('Yes')
        else:
            print('No')

