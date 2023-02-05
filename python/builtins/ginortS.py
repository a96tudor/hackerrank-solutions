if __name__ == '__main__':
    string = input()
    odd_digits = '13579'
    even_digits = '24680'

    lower_case = ''.join(sorted(c for c in string if c.islower()))
    upper_case = ''.join(sorted(c for c in string if c.isupper()))
    odd_digit = ''.join(sorted(c for c in string if c in odd_digits))
    even_digit = ''.join(sorted(c for c in string if c in even_digits))

    print(''.join((lower_case, upper_case, odd_digit, even_digit)))
