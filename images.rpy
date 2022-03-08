## jump to other conf files
"bin/gui_.rpy"
"bin/conf.rpy"
"bin/screens_.rpy"
"bin/characters_base.rpy"
"bin/functions.rpy"
"bin/transfoms.rpy"
"bin/images_python.rpy"

## common files
"characters.rpy"
"images.rpy"
"screens.rpy"

## script
"scripts/chapter1/1a_poczatek.rpy"

#notatki gowna bo sie pomylilam w przeszlosci pozdro mordo musi byc png
image lobby = Image("background/lobby.png")
image bg lobby = Image("background/lobby.png")
image defense = Image("background/defense.png")
image codefense = Image("background/codefense.png")
image judge = Image("background/judge.png")
image prosecution = Image("background/prosecution.png")
image coprosecution = Image("background/coprosecution.png")
image witness = Image("background/witness.png")
image courtroom = Image("background/courtroom.png")
image gavel = Image("background/gavel.jpg")

init python:
    transparenty_path = lambda x: "scenes/transparenty2/{}.png".format(x)

image bg transparenty11 = Image(transparenty_path("transparenty1"))

#image bg ulubione_filmy = Image("scenes/ulubione/ulubione_filmy.png")
#image bg ulubione = Image("scenes/ulubione/ulubione.png")
#image bg ulubione_powiedzenia = Image("scenes/ulubione/ulubione_powiedzenia.png")

image bg black = Image("background/black.png")
#image blur = Image("background/blur.png")

image minikonopski = Image("characters/konopski/mini-konopski.png")

image winny = Image("others/winny.png")

image reaction_luv = At("luv", beating)
image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)
image reaction_angry2 = At("angry2", beating)
image flowers:
    "flowers 1"
    ANIMATION_PAUSE
    "flowers 2"
    ANIMATION_PAUSE
    repeat
# Movies
image straszne = Movie("video/strasznego.mp4", (0,0), (0,0))
