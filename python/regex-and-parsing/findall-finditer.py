import re

if __name__ == '__main__':
    string = input()
    vowles  = '[AEIOUaeiou]{2,}'
    constants = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'

    # Regex
    regex = re.compile(rf'(?<={constants}){vowles}(?={constants})')
    result = re.findall(regex, string)
    if len(result) > 0:
        print('\n'.join(result))
    else:
        print(-1)
