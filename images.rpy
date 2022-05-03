"files_list.rpy"

#notatki gowna bo sie pomylilam w przeszlosci pozdro mordo musi byc png
#image lobby = Image("background/lobby.png")
image bg lobby = Image("background/lobby.png")
image lobby2 = Image("background/lobby2.png")
image lobby_black = Image("background/lobby_black.png")

image bg black = Image("background/black.png")

image minikonopski = Image("characters/konopski/mini-konopski.png")

image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)

image question = animation_reaction("question")
image flowers = animation_reaction("flowers")

init python:
    def reaction(name, fun=beating):
        renpy.show(name, at_list=[fun])

image reaction_switch = ShowingSwitch(
    "kropla", At("sweatdrop", dropping))
