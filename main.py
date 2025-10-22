from markdown import markdown
from pathlib import Path
import os

def toHtml(name):
    with open("md/" + name + ".md", "r", encoding="utf-8") as f:
        print("reading " + name)
        md = f.read()

    html = markdown(md, extensions=["tables", "sane_lists", "fenced_code"])
    with open("tmp/" + name + ".html", "w", encoding="utf-8") as f:
        print("writing " + name)
        f.write(html)

head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jonesangga's page</title>
    <style>
        html {
            padding: 0;
            margin: 0 auto;
            max-width: 700px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <a href="index.html">index</a> //
    <a href="links.html">links</a>
"""

def index():
    s = sorted(Path("tmp").iterdir(), key=lambda p: p.name, reverse=True)

    with open("index.html", "w", encoding="utf-8") as f:
        print("Merging to index.html")
        f.write(head)
        for file in s:
            data = file.read_text(encoding="utf-8")
            f.write(data)
            f.write("<hr>")
        f.write("</body></html>")

def posts():
    # Get all filenames in md/ directory.
    p = Path("md")
    mds = [f.name for f in p.iterdir() if f.is_file()]

    # Get filenames without extension
    for md in mds:
        html = md[:-3] + ".html"
        if not os.path.exists("tmp/" + html):
            print("     NEW " + md)
            toHtml(md[:-3])
        elif os.path.getmtime("md/" + md) > os.path.getmtime("tmp/" + html):
            print("  UPDATE " + md)
            toHtml(md[:-3])
        else:
            print("    PASS " + md)
    index()

def links():
    name = "links"
    with open(name + ".md", "r", encoding="utf-8") as f:
        print("reading " + name)
        md = f.read()

    html = markdown(md, extensions=["tables", "sane_lists", "fenced_code"])
    with open(name + ".html", "w", encoding="utf-8") as f:
        print("writing " + name)
        f.write(head)
        f.write(html)
        f.write("</body></html>")

def main():
    posts()
    #  links()


if __name__ == "__main__":
    main()
