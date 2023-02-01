if __name__ == '__main__':
    _ = input()
    a = list(map(int, input().split()))

    multiple_apps = {}

    for x in a:
        if x in multiple_apps:
            multiple_apps[x] = True
            continue
        multiple_apps[x] = False

    for x in multiple_apps:
        if not multiple_apps[x]:
            print(x)
            break

