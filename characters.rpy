init python:
    class Characterr:
        def __init__(self, name, who_color='#000000', start=(100,0), mouth=(0,0)):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.mouth_pos = Position(xpos=mouth[0], ypos=mouth[1])
            self.pos = start
            self.who_color = who_color
            self.show_args = [Transform(pos=start)]

            self.char = Character(name=self.capital_name, image=self.name, callback=partial(char_talking, self), who_color=who_color)

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

layeredimage wardega:
    group body auto:
        attribute main default

#    if WardegaC.talking:
#        WardegaC.mouth at WardegaC.mouth_pos

layeredimage konopski:
    group body auto:
        attribute main default

layeredimage revo:
    group body auto:
        attribute main default

layeredimage gimper:
    group body auto:
        attribute main default

layeredimage lexio:
    group body auto:
        attribute main default

define Dziewczyna1C = Characterr("Dziewczyna1")
define Dziewczyna1 = Dziewczyna1C.char

layeredimage dziewczyna1:
    group body auto:
        attribute main default

define Dziewczyna2C = Characterr("Dziewczyna2")
define Dziewczyna2 = Dziewczyna2C.char

layeredimage dziewczyna2:
    group body auto:
        attribute main default

define Dziewczyna3C = Characterr("Dziewczyna3")
define Dziewczyna3 = Dziewczyna3C.char

layeredimage dziewczyna3:
    group body auto:
        attribute main default
