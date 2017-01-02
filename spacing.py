import pangu
import sys


def main(argv):
    file = argv[0]
    with open(file, encoding='utf8') as r:
        content = r.read()
    with open(file, 'w', encoding='utf8') as w:
        content = pangu.spacing(content)
        # For markdown
        if file.endswith('.md'):
            content = content.replace(' ** ', '**') \
                             .replace('"/>', '" />') \
                             .replace(' “', '“') \
                             .replace('” ', '”') \
                             .replace('&emsp;&emsp; ', '&emsp;&emsp;') \
                             .replace('"alt', '" alt')
        w.write(content)

if __name__ == '__main__':
    main(sys.argv[1:])
