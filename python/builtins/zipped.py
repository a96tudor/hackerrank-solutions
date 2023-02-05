if __name__ == '__main__':
    _, x = tuple(map(int, input().split()))
    data = []

    for _ in range(x):
        data.append(list(map(float, input().split())))

    average_scores = [sum(t) / len(t) for t in zip(*data)]
    print('\n'.join(str(score) for score in average_scores))
