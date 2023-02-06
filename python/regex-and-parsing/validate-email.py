import re
import email.utils as utils

if __name__ == '__main__':
    regex = r'^[a-z][a-z0-9_\.\-]*@[a-z]+\.[a-z]{1,3}$'

    n = int(input())

    for _ in range(n):
        line = input()
        email = utils.parseaddr(line)[1]

        if re.match(regex, email):
            print(line)
