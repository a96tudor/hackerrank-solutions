from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    items = OrderedDict()

    for _ in range(n):
        data = input().split()
        price = int(data[-1])
        name = ' '.join(data[:-1])

        if name in items:
            items[name] += price
        else:
            items[name] = price

    print('\n'.join(' '.join([key, str(value)]) for key, value in items.items()))
