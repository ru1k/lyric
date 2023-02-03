import os


def iter_link(path):
    for filename in os.listdir(path):
        if not filename.startswith('_'):
            name, ext = os.path.splitext(filename)
            filename = filename.replace(" ", "%20")
            yield f'<a href="./{path}/{filename}"><h1>{name}</h1></a>'


def main():
    html = """<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <title>Lyric</title>
  <style>
    div {
      margin: auto;
      width: fit-content;
      font-size: 2em;
    }
  </style>
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
