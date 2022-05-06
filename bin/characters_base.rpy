"../files_list.txt"

init -8 python:
### CHARACTERS

    PATH_CHARACTERS = gpj("images", "characters")

    class CharacterBase:
        def __init__(self, name, styles=[], group="", blip=None):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.group = group

            self.talking = False
            self.blip = blip

        @property
        def char(self):
            return Character(
                name=self.capital_name,
                image=self.name,
                callback=partial(char_talking, self))

        @property
        def animations_switch(self):
            res = []
            for s in self.styles:
                res.extend(["{} {}".format(self.name, s), animation_maker(self.name, s)])
            res.extend(["True", animation_maker(self.name, "main")])
            return ShowingSwitch(*res)

        @property
        def character_path(self):
            return gpj(PATH_CHARACTERS, self.group, self.name)

        @property
        def styles(self):
            return [d for d in os.listdir(gpj(self.character_path, "animations"))]

        def __str__(self):
            return self.name
