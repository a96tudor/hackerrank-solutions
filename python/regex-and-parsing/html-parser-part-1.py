import html.parser as parser


class HTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for key, value in attrs:
            print(f'-> {key} > {value}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for key, value in attrs:
            print(f'-> {key} > {value}')


if __name__ == '__main__':
    n = int(input())

    lines = []
    for _ in range(n):
        lines.append(input())
    string = '\n'.join(lines)

    parser = HTMLParser()
    parser.feed(string)
