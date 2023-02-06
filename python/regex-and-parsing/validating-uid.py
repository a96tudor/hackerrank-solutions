import re
from collections import Counter

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        uid = ''.join(sorted(input()))

        try:
            assert re.search(r'[A-Z]{2,}', uid)
            assert re.search(r'[0-9]{3,}', uid)
            assert re.match(r'^[a-zA-Z0-9]{10}$', uid)
            counter = Counter(uid)
            assert not any(x > 1 for x in counter.values())

            print('Valid')
        except AssertionError:
            print('Invalid')
