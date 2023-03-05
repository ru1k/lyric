import os
from lxml import etree


def iter_lyric(path):
    example = load(f'{path}/.example.html')
    title = example.find('head/title')
    body = example.find('body')
    for filename in os.listdir(path):
        if not filename.startswith('.'):
            filename = f'{path}/{filename}'
            html = load(filename)
            title.text = html.find('head/title').text
            _body = html.find('body')
            example.replace(body, _body)
            body = _body
            for br in body.xpath('//td/br'):
                br.getparent().remove(br)
            dump(filename, example)
            yield f'<a href="{filename}"><h2>{title.text}</h2></a>'


def load(filename, parser=etree.HTMLParser(remove_comments=True)):
    return etree.parse(filename, parser).getroot()


def dump(filename, html):
    for e in html.iter():
        e.tail = None
        if e.text and e.tag not in ('h2', 'td'):
            e.text = e.text.strip() if e.tag != 'style' else e.text.replace(' ', '').replace('\r', '')
    b = etree.tostring(html, encoding='utf-8', method='html', doctype='<!DOCTYPE html>').replace(b'\n', b'')
    with open(filename, 'wb') as fp:
        fp.write(b)
    return


def css(filename):
    with open(filename) as fp:
        s = fp.read().replace(' ', '').replace('\n', '')
    with open(filename, 'w') as fp:
        fp.write(s)


def main():
    filename = 'index.html'
    html = load(filename)
    body = html.find('body')
    body.clear()
    body.append(etree.XML(f"<div>{''.join(iter_lyric('-'))}</div>"))
    dump(filename, html)
    css('style.css')


if __name__ == '__main__':
    main()
