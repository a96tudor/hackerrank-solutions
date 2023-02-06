import html.parser as parser


class HTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

        for key, value in attrs:
            print(f'-> {key} > {value}')


if __name__ == '__main__':
    n = int(input())
    html = '\n'.join(input() for _ in range(n))

    parser = HTMLParser()
    parser.feed(html)
    parser.close()
