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


image reaction_luv = At("luv", beating)
image reaction_sweatdrop = At("sweatdrop", dropping)
image reaction_angry = At("angry", beating)
image reaction_angry2 = At("angry2", beating)
