from collections import namedtuple

TextLine = namedtuple("TextLine", "character text style")

f_name = "text.txt"
def read_text():
    with open(f_name) as f:
        character = f.readline()
        style = f.readline()
        t = f.readlines()
        tt = TextLine(character, style, t)

read_text()
