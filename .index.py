import os
from lxml import etree


def iter_lyric(path):
    for filename in os.listdir(path):
        if not filename.startswith('.'):
            with open(os.path.join(path, filename), 'rb') as fp:
                html = etree.HTML(fp.read())
            title = html.find('./head/title').text
            yield f'<a href="./{path}/{filename}"><h2>{title}</h2></a>'


def to_bytes(html):
    for e in html.iter():
        if e.tail:
            e.tail = e.tail.strip()
        if e.text:
            e.text = e.text.strip() if e.tag != 'style' else e.text.replace(' ', '')
    return etree.tostring(html, encoding='utf-8', method='html', doctype='<!DOCTYPE html>').replace(b'\n', b'')


def main():
    tree = etree.HTML("""
<html>
    <head>
        <title>Lyric</title>
        <style>
            div {
                width: fit-content;
                margin: auto;
                padding-top: 1em;
                padding-bottom: 1em;
            }
        </style>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" />
    </head>
    <body>
      <div>
        %s
      </div>
    </body>
</html>
""" % ''.join(iter_lyric('-')))
    content = to_bytes(tree)
    with open('index.html', 'wb') as fp:
        fp.write(content)


if __name__ == '__main__':
    main()
