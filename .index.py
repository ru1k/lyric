import os
from lxml import etree


def iter_lyric(path):
    for filename in os.listdir(path):
        if not filename.startswith('.'):
            filename = f'./{path}/{filename}'
            with open(filename, 'rb') as fp:
                html = etree.HTML(fp.read())
            yield f'<a href="{filename}"><h2>{html.find("./head/title").text}</h2></a>'
            dump(filename, html)


def dump(filename, html):
    for e in html.iter():
        e.tail = None
        if e.text and e.tag not in ('h2', 'td'):
            e.text = e.text.strip()  # if e.tag != 'style' else e.text.replace(' ', '').replace('\r', '')
    b = etree.tostring(html, encoding='utf-8', method='html', doctype='<!DOCTYPE html>')  # .replace(b'\n', b'')
    with open(filename, 'wb') as fp:
        fp.write(b)
    return 


def main():
    filename = 'index.html'
    with open(filename, 'rb') as fp:
        html = etree.HTML(fp.read())
    body = html.find('body')
    body.clear()
    body.append(etree.XML(f"<div>{''.join(iter_lyric('-'))}</div>"))
    dump(filename, html)


if __name__ == '__main__':
    main()
