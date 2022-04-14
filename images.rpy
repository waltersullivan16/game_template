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
image lobby2 = Image("background/lobby2.png")
image lobby_black = Image("background/lobby_black.png")
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

image bg black = Image("background/black.png")

image minikonopski = Image("characters/konopski/mini-konopski.png")

image winny = Image("others/winny.png")
image reactions = ShowingSwitch(
    "kropla", At("sweatdrop", dropping),
    None, "null"
)
image reaction_luv = At("luv", beating)
image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)
image reaction_angry2 = At("angry2", beating)
image reaction_danger = At("danger", beating)

image question = animation_reaction("question")
image flowers = animation_reaction("flowers")

image straszne = Movie("video/strasznego.mp4", (0,0), (0,0))
init python:
    def reaction(name, fun=beating):
        renpy.show(name, at_list=[fun])

image reaction_switch = ShowingSwitch(
    "kropla", At("sweatdrop", dropping))
#image mini-konopski = 
