if __name__ == '__main__':
    _ = input()
    arr = [int(x) for x in input().split(' ')]
    n = set(int(x) for x in input().split(' '))
    m = set(int(x) for x in input().split(' '))

    n_intersect_m = m.intersection(n)
    n_diff_m = n.difference(m)
    m_diff_n = m.difference(n)

    happiness = 0

    for x in arr:
        if x in n_intersect_m:
            # We don't increase or decrease the happiness
            continue
        if x in n_diff_m:
            happiness += 1
            continue
        if x in m_diff_n:
            happiness -= 1

    print(happiness)
