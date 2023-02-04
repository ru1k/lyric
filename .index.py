import os
from lxml import etree


def iter_lyric(path):
    for filename in os.listdir(path):
        if not filename.startswith('.'):
            f = os.path.join(path, filename)
            with open(f, 'rb') as fp:
                html = etree.HTML(fp.read())
            output(f, html)
            title = html.find('./head/title').text
            yield f'<a href="./{path}/{filename}"><h2>{title}</h2></a>'


def output(filename, html):
    for e in html.iter():
        e.tail = None
        if e.text and e.tag not in ('h2', 'td'):
            e.text = e.text.strip() if e.tag != 'style' else e.text.replace(' ', '')
    b = etree.tostring(html, encoding='utf-8', method='html', doctype='<!DOCTYPE html>').replace(b'\n', b'')
    with open(filename, 'wb') as fp:
        fp.write(b)
    return 


def main():
    html = etree.HTML("""
<html>

<head>
    <meta charset="UTF-8">
    <title>Lyric</title>
    <style>
        div {
            width: fit-content;
            margin: auto;
            padding-top: 1em;
            padding-bottom: 1em;
        }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes">
</head>

<body>
    <div>
        %s
    </div>
</body>

</html>
""" % ''.join(iter_lyric('-')))
    output('index.html', html)


if __name__ == '__main__':
    main()
