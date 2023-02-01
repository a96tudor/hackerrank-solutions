from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    freq = OrderedDict()

    for _ in range(n):
        word = input()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(len(freq))
    print(' '.join(str(v) for v in freq.values()))
