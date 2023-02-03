import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    ac = math.sqrt(ab ** 2 + bc ** 2)
    print(f'{round(math.degrees(math.asin(ab / ac)))}{chr(176)}')
