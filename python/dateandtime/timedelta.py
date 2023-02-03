import datetime


def parse_and_transform(string):
    time_format = '%a %d %b %Y %H:%M:%S %z'

    return datetime.datetime.strptime(string, time_format).astimezone(datetime.timezone.utc)


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        t1 = parse_and_transform(input())
        t2 = parse_and_transform(input())

        print(int(abs(t1 - t2).total_seconds()))
