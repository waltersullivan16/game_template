init python:
    class Characterr:
        def __init__(self, name, who_color='#000000', start=(0,0), mouth=(0,0)):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.mouth_pos = Position(xpos=mouth[0], ypos=mouth[1])
            self.pos = Position(xpos=start[0], ypos=start[1])
            self.who_color = who_color

            self.char = Character(name=self.capital_name, callback=partial(char_talking, self), who_color=who_color)

            self.talking = False
            self.layeredimage = None

        def __str__(self):
            return self.name

        @property
        def coordinates(self):
            position_array = renpy.get_image_bounds(self.image)
            print(position_array)
            return [position_array[0], position_array[2]]

        @property
        def mouth(self):
            return Animation(*mouth_animation(self.name))
        #x = LayeredImage([Attribute("test", "main", "reaction_sweatdrop")])

define WardegaC = Characterr("Wardega")
define Wardega = WardegaC.char

define KonopskiC = Characterr("Konopski")
define Konopski = KonopskiC.char

define RevoC = Characterr("Revo")
define Revo = RevoC.char

define GimperC = Characterr("Gimper")
define Gimper = GimperC.char

define LexioC = Characterr("Lexio")
define Lexio = LexioC.char

define Dziewczyna1C = Characterr("Dziewczyna1")
define Dziewczyna1 = Dziewczyna1C.char

layeredimage wardega:
    group body auto:
        attribute main default

    if WardegaC.talking:
        WardegaC.mouth at WardegaC.mouth_pos

layeredimage konopski:
    group body auto:
        attribute main default

    if konopskic.talking:
        Konopskic.mouth at konopskic.mouth_pos

layeredimage revo:
    group body auto:
        attribute main default

    if RevoC.talking:
        RevoC.mouth at RevoC.mouth_pos

layeredimage gimper:
    group body auto:
        attribute main default

    if GimperC.talking:
        GimperC.mouth at GimperC.mouth_pos

layeredimage lexio:
    group body auto:
        attribute main default

    if LexioC.talking:
        LexioC.mouth at LexioC.mouth_pos

layeredimage dziewczyna1:
    group body auto:
        attribute main default

    if Dziewczyna1C.talking:
        Dziewczyna1C.mouth at Dziewczyna1C.mouth_pos


#notatki gowna bo sie pomylilam w przeszlosci pozdro mordo musi byc png
image lobby = Image("background/lobby.png")
#image x = Movie("x", (0,0), (0,0))
#image ekipup_text = comic_text_maker("EKIPUP")

image reaction_luv = At("luv", beating)
image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)
image reaction_angry2 = At("angry2", beating)
