def minion_game(string):
    scores = {
        'Stuart': 0,
        'Kevin': 0,
    }
    vowels = 'AEIOU'

    for idx in range(len(string)):
        if string[idx] in vowels:
            scores['Kevin'] += len(string) - idx
        else:
            scores['Stuart'] += len(string) - idx

    if scores['Stuart'] > scores['Kevin']:
        print(f'Stuart {scores["Stuart"]}')
    elif scores['Kevin'] > scores['Stuart']:
        print(f'Kevin {scores["Kevin"]}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
