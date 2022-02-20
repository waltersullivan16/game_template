## jump to other conf files
"bin/gui_.rpy"
"bin/conf.rpy"
"bin/characters_base.rpy"
"bin/functions.rpy"

## common files
"characters.rpy"
"images.rpy"

## script
"scripts/1_uwertura.rpy"

#notatki gowna bo sie pomylilam w przeszlosci pozdro mordo musi byc png
image lobby = Image("background/lobby.png")
image defense = Image("background/defense.png")
image codefense = Image("background/codefense.png")
image judge = Image("background/judge.png")
image prosecution = Image("background/prosecution.png")
image coprosecution = Image("background/coprosecution.png")
image witness = Image("background/witness.png")
image courtroom = Image("background/courtroom.png")
image gavel = Image("background/gavel.jpg")

image winny = Image("others/winny.png")

image reaction_luv = At("luv", beating)
image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)
image reaction_angry2 = At("angry2", beating)

image straszne = Movie("video/strasznego.mp4", (0,0), (0,0))
# Moves
init python:
    vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

    m = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

