#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()

    letters_freq = Counter(s)
    ordered = sorted(
        letters_freq.most_common(), key=lambda x: (-x[1], x[0])
    )
    print('\n'.join(
        ' '.join([x[0], str(x[1])]) for x in ordered[:3]
    ))
