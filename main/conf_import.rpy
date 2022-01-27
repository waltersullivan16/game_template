define WardegaC = Characterr("Wardega")
define Wardega = WardegaC.char

define KonopskiC = Characterr("Konopski")
define Konopski = KonopskiC.char

define Dziewczyna1C = Characterr("Dziewczyna1")
define Dziewczyna1 = Dziewczyna1C.char

layeredimage wardega:
    group body auto:
        attribute main default

    group reaction:
        attribute normal default null
        attribute luv:
            "reaction_luv"

#    if WardegaC.talking:
#        FrizClass.mouth at WardegaC.mouth_pos
init python:
    class Picker(object):
        def __init__(self, options=[]):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)
            print("DDADASD",attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

                return rv

layeredimage dziewczyna1:
    attribute_function Picker()
    group body auto:
        attribute maddin default

layeredimage konopski:
    group bodky auto:
        attribute main default

#    if WardegaC.talking:
#        FrizClass.mouth at WardegaC.mouth_pos

#notatki gowna bo sie pomylilam w przeszlosci pozdro mordo musi byc png
image lobby = Image("background/lobby.png")
#image x = Movie("x", (0,0), (0,0))
#image ekipup_text = comic_text_maker("EKIPUP")
