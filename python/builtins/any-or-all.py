def is_palindrome(x):
    rev = 0
    x1 = x

    while x1 > 0:
        rev = (rev * 10) + (x1 % 10)
        x1 //= 10

    return rev == x


if __name__ == '__main__':
    _ = input()

    arr = list(map(int, input().split()))

    if all(x >= 0 for x in arr):
        print(any(is_palindrome(x) for x in arr))
    else:
        print(False)
