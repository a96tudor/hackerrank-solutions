cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    result = [0, 1]

    for _ in range(2, n):
        result.append(result[-1] + result[-2])

    return result


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
