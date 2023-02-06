from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.split('\n')
        if len(lines) == 1:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')

        print(data)

    def handle_data(self, data):
        if not data.isspace():
            print(f'>>> Data\n{data}')


if __name__ == '__main__':

    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
