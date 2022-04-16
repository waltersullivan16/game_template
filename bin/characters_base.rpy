"../files_list.txt"

init -8 python:
### CHARACTERS

## SPECIAL CHARACTERS
    PATH_CHARACTERS = gpj("images", "characters")

    class CharacterBase:
        def __init__(self, name, styles=[], who_color='#000000', group="", blip=None):
            self.capital_name = name.upper()
            self.name = name.lower()

            #self.mouth_pos = mouth_pos
            #self.pos = start
            #self.who_color = who_color
            #self.show_args = [Transform(pos=start)]
            self.group = group

            self.talking = False
            self.blip = blip

        @property
        def char(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self))
                #who_color=self.who_color)
        @property
        def animations_switch(self):
            res = []
            for s in self.styles:
                res.extend(["{} {}".format(self.name, s), animation_maker(self.name, s)])
            return ShowingSwitch(*res)

        @property
        def character_path(self):
            return gpj(PATH_CHARACTERS, self.group, self.name)

        @property
        def styles(self):
            return [d for d in os.listdir(gpj(self.character_path, "animations"))]

        def __str__(self):
            return self.name
