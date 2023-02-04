import os


def iter_link(path):
    for filename in os.listdir(path):
        if not filename.startswith('_'):
            name, ext = os.path.splitext(filename)
            yield f'<a href="./{path}/{filename}"><h2>{name}</h2></a>'


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
    with open('index.html', 'w', encoding='utf8') as fp:
        fp.write(html)


if __name__ == '__main__':
    main()
