COMMANDS = {
    'insert': lambda arr, x, y: arr.insert(x, y),
    'append': lambda arr, x, _: arr.append(x),
    'remove': lambda arr, x, _: arr.remove(x),
    'sort': lambda arr, _, __: arr.sort(),
    'pop': lambda arr, _, __: arr.pop(),
    'reverse': lambda arr, _, __: arr.reverse(),
    'print': lambda arr, _, __: print(arr)
}

if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        data = input()

        data_split = data.split()

        command = data_split[0]
        try:
            x = int(data_split[1])
        except IndexError:
            x = None

        try:
            y = int(data_split[2])
        except IndexError:
            y = None

        COMMANDS[command](arr, x, y)
