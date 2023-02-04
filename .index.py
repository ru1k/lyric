import os
from lxml import etree


def iter_link(path):
    for filename in os.listdir(path):
        if not filename.startswith('_'):
            with open(os.path.join(path, filename), encoding='utf-8') as fp:
                html = etree.HTML(fp.read())
            title = html.find('./head/title').text
            yield f'<a href="./{path}/{filename}"><h2>{title}</h2></a>'


def main():
    html = """<!DOCTYPE html>
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
""" % '\n'.join(iter_link('-'))
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(html)


if __name__ == '__main__':
    main()
